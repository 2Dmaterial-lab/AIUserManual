# 更新日志

记录手册的主要修订，便于读者判断内容新鲜度。细则修改不必逐条列出。

| 日期 | 摘要 |
|------|------|
| 2026-04-12 | **内容与结构**：《AI 工具选择与使用指南》扩充（多类产品、费用与隐私提示、科研软件配合等）；新增「课题组信息与本地约定」；首页按角色入口、前言典型误区；各章统一导读与提示词章内导航；Excel / SolidWorks 章节编号统一为阿拉伯数字；课题组信息移至独立附录；补充 `docs/assets/test_data/` 与 MATLAB 示例；新增 `LICENSE`；版权年份改为 2025–2026。 |
| 2026-04-12 | **站点与主题**：配置 `site_url` / `repo_url`、页脚版权与「在 GitHub 上编辑」；启用 `navigation.tracking`、`toc.follow`；`mkdocs-redirects` 与 `content.code.annotate`；固定 `requirements.txt` 中 MkDocs / Material 版本；仓库 public 后移除全站 `noindex`；README / CONTRIBUTING 与首页提示、目录及许可说明对齐。 |
| 2026-04-12 | **访问统计与页脚**：可选 GA4（`extra.analytics` + `GOOGLE_ANALYTICS_ID`，无 ID 不注入脚本）；全站累计浏览由 `scripts/fetch_ga_stats.py` 经 GA4 Data API 写入 `docs/assets/analytics-stats.json` 并覆盖页脚；`eventCount` 优先用语义为 `page_view` 的维度过滤，为 0 时再试 `screenPageViews`；页脚用站点绝对 URL 拉取 JSON，含加载中/失败/零值说明；部署需 `GA_SERVICE_ACCOUNT_JSON`、`GA4_PROPERTY_ID` 与 `google-analytics-data`，README 含 GCP/GA 授权步骤。 |
| 2026-04-12 | **部署与 CI**：工作流支持 `workflow_dispatch` 与定时任务（含 UTC 整点每小时同步页脚累计、以及每日构建）；`paths` 含 `README.md` 以便说明变更也走发布；pip 缓存；CI 增加 `lychee` 外链检查（不阻断合并）；README 说明 JSON 仅在部署时更新，真·实时统计需自建 API。 |
