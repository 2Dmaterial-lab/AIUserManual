import tempfile
import unittest
from pathlib import Path
from scripts.check_site import check


class SiteLinksTest(unittest.TestCase):
    def test_nested_links_unicode_anchor_and_assets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'chapter').mkdir()
            (root / 'assets').mkdir()
            (root / 'assets/data.json').write_text('{}')
            (root / 'index.html').write_text('<a href="chapter/#%E6%A8%A1%E5%9E%8B">Read</a>')
            (root / 'chapter/index.html').write_text('<h1 id="模型">Title</h1><a href="../">Home</a><div data-stats="../assets/data.json"></div>')
            self.assertEqual(check(root, 'https://example.org/manual/'), ([], 2))

    def test_missing_page_anchor_and_asset_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'index.html').write_text('<a href="missing/">Page</a><a href="#absent">Anchor</a><script src="missing.js"></script>')
            errors, count = check(root, 'https://example.org/manual/')
            self.assertEqual(count, 1)
            self.assertEqual(len(errors), 3)

    def test_external_links_are_not_claimed_as_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'index.html').write_text('<a href="https://other.org/missing">External</a>')
            self.assertEqual(check(root, 'https://example.org/manual/'), ([], 1))

    def test_empty_build_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(check(tmp, 'https://example.org/manual/')[0])
