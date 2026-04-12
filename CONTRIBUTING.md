# 如何贡献与反馈

本手册由课题组成员共同维护，欢迎纠错与补充。

## 反馈渠道

- **错字、失效链接、过时描述**：可在仓库中提 Issue，或直接联系当前维护同学。
- **希望增加的工具或场景**：说明使用背景与期望内容，便于他人接手编写。

## 提交修改时的约定

1. **小改动**：修正笔误、更新链接，可直接提交到 `main`（或通过 Pull Request）。
2. **新增章节或大块内容**：尽量保持与现有章节一致的结构（参见各工具章开头的「本章导读」与仓库 `README.md` 中的说明）。
3. **可下载脚本**：放入 `docs/assets/examples/`，文件名使用小写字母与下划线，并在对应章节的「进阶资源」中说明用途。
4. **涉及价格、产品名、政策**：在文内注明「请以官网为准」。凡更新《AI工具选择与使用指南》中的产品表、费用或注册步骤，请**同步**：（1）调整 `docs/01-ai-tools-guide.md` 顶部「价格与产品信息时效」中的核对说明或日期；（2）在 `docs/changelog.md` 增加一条摘要，便于读者判断内容新鲜度。

## 主题与全站行为

- **Material 覆盖**：目录 `overrides/` 中的模板会覆盖主题默认实现（例如 `partials/integrations/analytics/google.html`：仅当配置了 `GOOGLE_ANALYTICS_ID` 时才注入 GA4 脚本）。修改后务必本地执行 `mkdocs build --strict`，并在变更可见时记入 `docs/changelog.md`。
- **访问统计（gtag）**：配置 **`GOOGLE_ANALYTICS_ID`**（GA4 衡量 ID `G-…`）。未配置时构建产物不含前端统计脚本。  
- **页脚浏览量汇总**：若需在站点展示「全站累计约 ×× 次页面浏览」，另需 **`GA_SERVICE_ACCOUNT_JSON`**（GCP 服务账号 JSON 全文）与 **`GA4_PROPERTY_ID`**（数字媒体资源 ID）；详见根目录 `README.md`。勿将 JSON 密钥写入仓库。
- **依赖版本**：`requirements.txt` 中已固定 `mkdocs` / `mkdocs-material` 主版本，便于 CI 与本地一致。升级主题或 MkDocs 时请在说明中写清，并全站预览后再合并。

## 本地检查

```bash
pip install -r requirements.txt
mkdocs build --strict
```

构建无告警后再推送，可避免线上部署失败。
