# 更新日志

记录手册的主要修订，便于读者判断内容新鲜度。细则修改不必逐条列出。

| 日期 | 摘要 |
|------|------|
| 2026-04-12 | 部署定时任务改为每小时（UTC 整点）同步页脚累计；README 说明真·实时需自建 API、可自调 cron。 |
| 2026-04-12 | 部署工作流增加 `workflow_dispatch` 与每日 `cron`（UTC 02:40），便于刷新页脚累计；README 说明 JSON 仅在部署时更新。 |
| 2026-04-12 | `fetch_ga_stats`：累计浏览改用语义为 `page_view` 的 `eventCount`（`dimension_filter`），避免仅 `screenPageViews` 在网页属性上长期为 0；仍为 0 时再试 `screenPageViews`。 |
| 2026-04-12 | 页脚浏览量：改为 `site_url` 绝对路径拉取 JSON（避免 instant 导航下相对路径失败）；加载中/失败/未配置时有提示；累计为 0 时附加说明（新站或 GA 延迟）。 |
| 2026-04-12 | 页脚展示「全站累计约 ×× 次页面浏览」：`scripts/fetch_ga_stats.py` + GA4 Data API 写入 `docs/assets/analytics-stats.json`；覆盖 `partials/copyright.html`；CI/部署安装 `google-analytics-data`；需 Secrets `GA_SERVICE_ACCOUNT_JSON` 与 `GA4_PROPERTY_ID`；README 增补 GCP/GA 授权步骤。 |
| 2026-04-12 | 可选访问统计：Material 集成 GA4（`extra.analytics` + `GOOGLE_ANALYTICS_ID`）；`overrides/partials/.../google.html` 在无 ID 时不输出脚本；部署工作流注入 Secret；README / CONTRIBUTING 补充配置说明。 |
| 2026-04-12 | Excel / SolidWorks 章节编号统一为阿拉伯数字；导航结构调整（课题组信息移至独立附录篇）；添加 MATLAB 示例脚本配套测试数据（`docs/assets/test_data/`）；添加 LICENSE 文件；版权年份改为区间格式（2025–2026）；添加 mkdocs-redirects 插件与 content.code.annotate 扩展；移除 noindex（仓库已 public，noindex 无实际保护作用）；更新 README 目录结构与测试数据说明。 |
| 2026-04-12 | 部署工作流 `paths` 增加 `README.md`，仅修改仓库说明时也会执行构建与 `gh-deploy`（站点 HTML 通常不变，但与「面向协作者的说明」变更保持发布流程一致）。 |
| 2026-04-12 | 固定 `requirements.txt` 中 MkDocs 与 Material 版本；主题启用 `navigation.tracking` 与 `toc.follow`；`CONTRIBUTING` 补充「主题与全站行为」说明。 |
| 2026-04-12 | 站点配置：`site_url` / `repo_url` /「在 GitHub 上编辑」、页脚版权；通过主题覆盖 `overrides/main.html` 注入全站 `noindex`；移除未使用的 `arithmatex`；README 目录对齐 nav 并补充许可与可见性说明；首页提示与 CONTRIBUTING 约定同步；CI 增加 pip 缓存与 lychee 外链检查（不阻断合并）；部署增加路径过滤与 pip 缓存。 |
| 2026-04-12 | 新增「课题组信息与本地约定」页；首页增加按角色快速入口；前言补充典型误区；AI 工具章增加价格核对说明；提示词章增加本页导航；各工具章增加统一导读；补充 CI 构建检查与贡献说明。 |
| 2026-04-12 | 《AI工具选择与使用指南》扩充：对话式产品补充 Gemini、Perplexity、Microsoft Copilot、Kimi、通义千问等；编程辅助补充 Codeium、JetBrains AI、Amazon Q；扩展费用速查、注册步骤、隐私「联网检索」提示及科研软件配合表。 |
