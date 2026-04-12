#!/usr/bin/env python3
"""
在部署前从 GA4 Data API 拉取全站累计 screenPageViews，写入 docs/assets/analytics-stats.json。
需要环境变量：
  GA_SERVICE_ACCOUNT_JSON  服务账号 JSON 全文（与 GitHub Secret 一致）
  GA4_PROPERTY_ID          纯数字，如 123456789（GA「管理 → 媒体资源设置」中的媒体资源 ID）

未设置上述变量时：写入占位 JSON，不报错（便于本地构建）。
已设置但 API 失败时：退出码非 0，以便 CI 可见。
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "docs", "assets", "analytics-stats.json")


def write_file(payload: dict) -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main() -> int:
    creds = (os.environ.get("GA_SERVICE_ACCOUNT_JSON") or "").strip()
    prop = (os.environ.get("GA4_PROPERTY_ID") or "").strip()

    if not creds or not prop:
        write_file(
            {
                "totalPageViews": None,
                "updatedAt": None,
                "source": "ga4",
                "note": "未配置 GA_SERVICE_ACCOUNT_JSON 或 GA4_PROPERTY_ID；部署时在 Actions 中设置 Secret 后即可显示约计浏览量。",
            }
        )
        return 0

    if not prop.isdigit():
        print("GA4_PROPERTY_ID 应为纯数字（媒体资源 ID）", file=sys.stderr)
        return 1

    cred_path = None
    try:
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
        tmp.write(creds)
        tmp.close()
        cred_path = tmp.name

        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import DateRange, Metric, RunReportRequest

        client = BetaAnalyticsDataClient.from_service_account_json(cred_path)
        request = RunReportRequest(
            property=f"properties/{prop}",
            date_ranges=[DateRange(start_date="2020-01-01", end_date="today")],
            metrics=[Metric(name="screenPageViews")],
        )
        response = client.run_report(request)
        if not response.rows:
            total = 0
        else:
            total = int(response.rows[0].metric_values[0].value)

        now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        write_file(
            {
                "totalPageViews": total,
                "updatedAt": now,
                "source": "ga4",
                "note": "自 2020-01-01 起至「今天」的 screenPageViews 合计；由部署任务拉取。",
            }
        )
        return 0
    except Exception as e:
        print(f"GA4 Data API 错误: {e}", file=sys.stderr)
        return 1
    finally:
        if cred_path and os.path.isfile(cred_path):
            try:
                os.unlink(cred_path)
            except OSError:
                pass


if __name__ == "__main__":
    sys.exit(main())
