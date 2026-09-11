# 更新日志

记录手册的主要修订，便于读者判断内容新鲜度。细则修改不必逐条列出。

| 日期 | 摘要 |
|------|------|
| 2026-09-11 | **内容核对**：刷新 Claude、OpenAI、DeepSeek 和 Gemini 官方模型目录，区分网页/API/Preview；替换过时的 CLI 与 Codeium 说明；修正学生权益、订阅与 API 费用边界，补充带链接的核对来源。前言与首页同步更新。 |
| 2026-09-11 | **科研软件维护**：核对 Origin 2026b 与学习版限制、MATLAB Copilot 条件、Excel Copilot 编辑模式、COMSOL 6.4 Update 3 与 Chatbot、Lumerical 2026 R1.4、SOLIDWORKS 学生产品、Cinema 4D/Redshift 更新、LabVIEW 2026 Q3 的 Nigel AI；更新手册仓库归属说明。示例脚本尚未在各商业软件内重新执行。 |
| 2026-09-11 | **站点维护**：修复 Maxon 教育入口与 SCPI 规范两处失效链接；修复版权配置与页脚统计在本地预览、即时导航中的初始化；无统计数据时隐藏计数。增加站内文件/锚点/资源检查及页脚回归测试；部署串行执行，可选 GA4 请求失败时仍发布正文；PR 构建不注入统计凭据。 |
| 2026-05-19 | **工具指南实用场景增强**：《AI工具选择与使用指南》新增科研软件工具选择速查、推荐工作流和 AI 配合方式分层；Origin、MATLAB、Excel、COMSOL、FDTD、SolidWorks、C4D、LabVIEW 各章新增「什么时候优先用」「AI 能做 / 不能做」「最小闭环案例」，帮助读者从实际任务判断工具选择、AI 边界和结果验收方式。 |
| 2026-05-19 | **科研工作流增强**：新增《科研任务工作流》，按文献调研、原始数据到论文图、仿真参数扫描、仪器自动化记录和投稿前检查组织任务；新增《数据管理与可复现科研》，补充目录结构、README 模板、原始数据保护、脚本复现清单、论文图追溯和 AI 使用记录；新增《入组第一周训练》，提供新生 5 天训练路线；首页、README、导航和《课题组信息与本地约定》同步增加任务入口；修正 SolidWorks 章节小节编号。 |
| 2026-05-19 | **全站 AI 信息刷新**：《AI工具选择与使用指南》按 2026-05-19 公开资料更新：代表模型线同步至 GPT-5.5、Claude Opus 4.7 / Sonnet 4.6、DeepSeek V4-Pro / V4-Flash、Gemini 3.1 Pro / Flash-Lite，并新增 GLM-5.1；新增 Grok、豆包、元宝等工具条目；新增「MCP协议与AI智能体」小节、科研工作流建议和本次核对来源；编程工具新增 Claude Code / Codex CLI 等终端工具对比；费用表改为更耐维护的套餐说明；《前言》新增「2026年AI新范式」小节（推理模型、Agent、MCP）；新增提问原则 6（推理模式）和隐私保护方案（本地模型 + MCP）；《提示词模板》新增推理/Agent、可复现数据分析、文献证据表、AI 使用记录与投稿声明等模板并更新导航与索引。 |
| 2026-04-12 | **站点与主题**：配置 `site_url` / `repo_url`、页脚版权与「在 GitHub 上编辑」；启用 `navigation.tracking`、`toc.follow`；`mkdocs-redirects` 与 `content.code.annotate`；固定 `requirements.txt` 中 MkDocs / Material 版本；仓库 public 后移除全站 `noindex`；README / CONTRIBUTING 与首页提示、目录及许可说明对齐。 |
| 2026-04-12 | **访问统计与页脚**：可选 GA4（`extra.analytics` + `GOOGLE_ANALYTICS_ID`，无 ID 不注入脚本）；全站累计浏览由 `scripts/fetch_ga_stats.py` 经 GA4 Data API 写入 `docs/assets/analytics-stats.json` 并覆盖页脚；`eventCount` 优先用语义为 `page_view` 的维度过滤，为 0 时再试 `screenPageViews`；页脚用站点绝对 URL 拉取 JSON，含加载中/失败/零值说明；部署需 `GA_SERVICE_ACCOUNT_JSON`、`GA4_PROPERTY_ID` 与 `google-analytics-data`，README 含 GCP/GA 授权步骤。 |
| 2026-04-12 | **部署与 CI**：工作流支持 `workflow_dispatch` 与定时任务（含 UTC 整点每小时同步页脚累计、以及每日构建）；`paths` 含 `README.md` 以便说明变更也走发布；pip 缓存；CI 增加 `lychee` 外链检查（不阻断合并）；README 说明 JSON 仅在部署时更新，真·实时统计需自建 API。 |
