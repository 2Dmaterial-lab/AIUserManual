#!/usr/bin/env python3
"""Check built HTML links, anchors and local assets without network access."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import argparse
import sys


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        for key in ('href', 'src', 'data-stats'):
            if attrs.get(key) and (key != 'href' or tag in ('a', 'link')):
                self.links.append(attrs[key])


def check(site, base_url):
    site = Path(site).resolve()
    base = urlsplit(base_url.rstrip('/') + '/')
    pages = {p: Page(p.read_text(encoding='utf-8')) for p in site.rglob('*.html')}
    if not pages:
        return ['No built HTML found; run mkdocs build --strict first.'], 0
    errors = set()
    for path, page in pages.items():
        relative = path.relative_to(site).as_posix()
        page_url = base_url.rstrip('/') + '/' + relative
        if page_url.endswith('index.html'):
            page_url = page_url[:-10]
        for link in page.links:
            target = urlsplit(urljoin(page_url, link))
            if target.scheme not in ('http', 'https') or target.netloc != base.netloc:
                continue
            if not target.path.startswith(base.path):
                errors.add(f'{relative}: link escapes site base: {link}')
                continue
            local = (site / unquote(target.path[len(base.path):])).resolve()
            if site not in local.parents and local != site:
                errors.add(f'{relative}: link escapes build directory: {link}')
                continue
            if local.is_dir():
                local /= 'index.html'
            if not local.is_file():
                errors.add(f'{relative}: missing target: {link}')
            elif target.fragment and local in pages and unquote(target.fragment) not in pages[local].ids:
                errors.add(f'{relative}: missing anchor: {link}')
    return sorted(errors), len(pages)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', nargs='?', default='site')
    parser.add_argument('--base-url', default='https://2dmaterial-lab.github.io/AIUserManual/')
    args = parser.parse_args()
    errors, count = check(args.site, args.base_url)
    for error in errors:
        print(error, file=sys.stderr)
    print(f'Checked {count} HTML pages: {len(errors)} broken local links/anchors/assets.')
    sys.exit(bool(errors))
