# AI工具选择与使用指南

目前市面上的 AI 工具大致分两类：**对话式 AI**（你问它答）和**编程辅助 AI**（嵌入编辑器实时辅助）。本章帮你搞清楚用哪个、怎么用。

!!! info "价格与产品信息时效"

    **以下价格、免费额度与产品名称已于 2026 年 4 月核对**，厂商政策与定价变化频繁。订阅、选课或申请教育优惠前，**务必以各产品官网当日说明为准**；建议与 [课题组信息与本地约定](11-lab-info.md) 中的账号说明对照使用。

---

## 一、对话式AI对比

下表先列出三款常用对话产品；更多国际与国内选择见本节 **「其他主流选择」**。

| 特性 | Claude | ChatGPT | DeepSeek |
|------|--------|---------|----------|
| **开发商** | Anthropic | OpenAI | DeepSeek |
| **强项** | 长文本理解、代码质量、遵循指令 | 生态最全、插件丰富、GPT-4o多模态 | 代码能力强、中文理解好、性价比高 |
| **弱项** | 插件生态不如ChatGPT | 代码有时"自信地犯错" | 创意写作和复杂推理稍弱 |
| **免费额度** | 有（有限） | 有（GPT-4o mini） | 有（较充裕） |
| **学生优惠** | 暂无 | ChatGPT Edu（部分学校） | 暂无 |
| **推荐场景** | 代码生成、长文档分析、科研写作 | 通用问答、多模态任务、插件调用 | 日常编程、代码调试、中文任务 |

### 其他主流选择

下表补充常见国际与国内网页对话产品，可与上表三款搭配使用；能力边界与可用地区**以各产品官网为准**。

| 工具 | 类型 | 强项 | 注意 |
|------|------|------|------|
| **Google Gemini** | 国际 | 与 Google 账号及搜索/Workspace 生态结合；多模态与长上下文常见 | 可用范围、套餐名随地区与政策变化 |
| **Perplexity** | 国际 | 检索增强、回答常附引用链接，适合快速查证与入门线索 | **不能替代**正式文献检索与数据库综述；联网场景注意第四节隐私 |
| **Microsoft Copilot** | 国际（网页/Windows/Edge） | 与 Microsoft 账号、Edge、Windows、Office 生态集成 | 功能随系统版本与 Microsoft 365 等订阅变化 |
| **Kimi**（月之暗面） | 国内常用 | 长文本、中文场景常见 | 额度与模型版本以官网为准 |
| **通义千问（Qwen）** | 国内常用 | 中文与阿里生态、工具调用等场景常见 | 以阿里云/通义官网能力与条款为准 |

### 选择建议

- **写 MATLAB/Python 代码**：Claude 和 DeepSeek 都不错，Claude 在复杂逻辑上更稳
- **处理中文文档/翻译**：DeepSeek 中文处理出色；也可结合 **通义千问**、**Kimi**
- **需要看图分析**：ChatGPT (GPT-4o) 的多模态能力强；已用 Google 生态可对比 **Gemini**
- **长文档阅读（论文）**：Claude 的长上下文窗口是优势；长中文材料可对比 **Kimi**
- **需要「带出处」的快速查证**：可考虑 **Perplexity**（仍须用正式数据库与综述核对）
- **已深度使用 Google / Microsoft 账号**：可优先考虑 **Gemini** 或 **Microsoft Copilot**，减少账号割裂
- **日常随手问**：哪个方便用哪个，差异不大
- **涉密、未发表数据、课题组未公开成果**：一律勿输入云端工具；见第四节

### 费用参考（2026年初）

| 产品 | 免费版 | 付费版（月费） |
|------|--------|----------------|
| Claude | 有限免费（Sonnet） | Pro $20/月（Opus） |
| ChatGPT | 免费（GPT-4o mini） | Plus $20/月（GPT-4o） |
| DeepSeek | 免费 | 暂无付费版 |

### 扩展工具费用速查

以下档位变化快，**仅列常见形态**；订阅前请以官网当日页面为准。

| 产品 | 说明（以官网为准） |
|------|-------------------|
| Gemini | 常见为免费档 + Google AI Pro 等付费档 |
| Perplexity | 常见为免费档 + Pro 等订阅档 |
| Microsoft Copilot | 免费能力与付费/365 捆绑因地区与套餐而异 |
| Kimi | 额度与会员以 [kimi.moonshot.cn](https://kimi.moonshot.cn) 当日说明为准 |
| 通义千问 | 以阿里云/通义官网当日定价与额度为准 |

> 建议：先用免费版熟悉，确认有持续需求再考虑付费。科研中 Claude Pro 或 ChatGPT Plus 的投资通常很值得。

> **时效性说明**：各产品名称、定价与政策会随厂商调整而变化，请以官方网站当日公布为准；本手册中的价格与功能描述仅作参考，建议每学期核对一次。

---

## 二、编程辅助AI对比

| 特性 | GitHub Copilot | Cursor | Windsurf |
|------|---------------|--------|----------|
| **形态** | VS Code/JetBrains 插件 | 独立IDE（基于VS Code） | 独立IDE |
| **核心功能** | 代码补全、Chat | 代码补全、Chat、项目级理解 | 代码补全、Chat、Flow |
| **强项** | 与GitHub深度集成、稳定性好 | 项目上下文理解强、编辑体验好 | 实时多文件编辑、上手快 |
| **弱项** | 缺少项目级上下文 | 需要迁移到新IDE | 生态较新 |
| **学生优惠** | 有（GitHub Education） | 暂无 | 暂无 |
| **适合谁** | 已有VS Code习惯的人 | 想要深度AI辅助的人 | 想要轻量AI辅助的人 |

### 其他常见形态

不想换主编辑器、或惯用 JetBrains 时，可考虑下列形态；产品名与功能以官网为准。

| 工具 | 形态 | 适合谁 | 说明 |
|------|------|--------|------|
| **Codeium** | VS Code、JetBrains、Vim 等多编辑器插件 | 需要免费档较常见的补全/聊天、**不愿换 IDE** | 与 Copilot 类似偏「插件补全」，深度项目级能力因编辑器而异 |
| **JetBrains AI Assistant / Junie** | 内置于 IntelliJ IDEA、PyCharm 等 JetBrains IDE | **坚持用 JetBrains 栈**、不迁到 VS Code 的用户 | 具体功能名（如 Assistant、Junie）与订阅以 [jetbrains.com/ai](https://www.jetbrains.com/ai/) 为准 |
| **Amazon Q Developer** | AWS 工具链与多款 IDE 插件 | 深度使用 **AWS** 的开发者 | 与云资源、IAM 策略相关，以 AWS 官网说明为准 |

### 选择建议

- **MATLAB 编程**：Copilot 不直接支持 MATLAB，用 Cursor + 对话式 AI 更实际；用 JetBrains 写脚本时可搭配 **JetBrains AI** + 对话式 AI
- **Python/LabVIEW脚本**：Copilot、Cursor、Codeium 或 JetBrains 内 AI 均可，按现有 IDE 选
- **VBA/Excel**：Copilot 支持较好；主要在 Office 内工作时也可结合 **Microsoft Copilot**（第一节）做问答，与编辑器插件分工
- **日常多语言**：Cursor 的项目级理解能力更全面；仅要补全可考虑 **Codeium** 等插件
- **不换编辑器、只要补全/Chat**：优先 **GitHub Copilot**、**Codeium** 等插件类
- **云 API、数据出境或合规敏感**：与第四节「本地部署」、课题组规定结合，谨慎选择联网助手

### 费用参考

| 产品 | 个人版 | 学生版 |
|------|--------|--------|
| GitHub Copilot | $10/月 | 免费（GitHub Education） |
| Cursor | $20/月 | 暂无 |
| Windsurf | 有免费额度 | 暂无 |
| Codeium | 常见有免费档，团队/企业档见官网 | 见官网 |
| JetBrains AI | 常与 IDE 订阅或单独 AI 订阅绑定 | 见官网 |

> 强烈建议：先注册 GitHub Education（只需学校邮箱），免费获得 Copilot。

> 编程类工具的月费、学生政策同样可能变更，以 GitHub、Cursor、Windsurf、Codeium、JetBrains 等官网为准。

---

## 三、账号注册快速指南

### GitHub Education（强烈推荐）

1. 访问 [education.github.com](https://education.github.com)
2. 用学校邮箱注册/登录 GitHub
3. 上传学生证明（学生证照片或学信网截图）
4. 审核通过后，在权益页面激活 Copilot

### Claude

1. 访问 [claude.ai](https://claude.ai)
2. 注册账号（可用 Google 登录）
3. 免费版即可使用 Claude Sonnet

### ChatGPT

1. 访问 [chat.openai.com](https://chat.openai.com)
2. 注册账号
3. 免费版使用 GPT-4o mini，Plus 订阅使用 GPT-4o

### DeepSeek

1. 访问 [chat.deepseek.com](https://chat.deepseek.com)
2. 注册账号
3. 免费使用，额度较充裕

### Google Gemini

1. 访问 [gemini.google.com](https://gemini.google.com)（若所在地区入口不同，以 Google 官方说明为准）
2. 使用 Google 账号登录
3. 免费档与付费档以页面当日说明为准

### Perplexity

1. 访问 [perplexity.ai](https://www.perplexity.ai)
2. 注册账号（可用常见邮箱或第三方登录，以官网为准）
3. 免费与 Pro 额度以官网当日说明为准

### Microsoft Copilot

1. 访问 [copilot.microsoft.com](https://copilot.microsoft.com)，或在 Windows、Edge 中打开 Copilot 入口
2. 使用 Microsoft 账号登录
3. 功能与是否需 Microsoft 365 等以微软官网当日说明为准

### Kimi

1. 访问 [kimi.moonshot.cn](https://kimi.moonshot.cn)
2. 按页面指引注册或登录
3. 额度与会员政策以官网当日说明为准

### 通义千问

1. 访问 [通义官网对话入口](https://tongyi.aliyun.com)（或阿里云控制台中的通义产品页）
2. 使用阿里云/淘宝等账号登录（以页面要求为准）
3. 额度与条款以官网当日说明为准

### Codeium

1. 访问 [codeium.com](https://codeium.com)
2. 注册账号后在目标编辑器中安装 Codeium 插件并按向导登录
3. 免费与团队政策以官网为准

### JetBrains AI

1. 打开 JetBrains IDE，在 **Plugins** 中搜索 **AI Assistant** 等官方 AI 插件，或访问 [jetbrains.com/ai](https://www.jetbrains.com/ai/)
2. 使用 JetBrains Account 登录并按向导启用
3. 试用、订阅与功能名以官网当日说明为准

---

## 四、隐私与安全

### 什么数据可以输入

- 公开数据集
- 已发表的实验数据
- 通用的代码片段
- 报错信息和日志
- 学习笔记和问题

### 什么数据绝对不能输入

- **未发表的实验数据**：可能被用于训练模型
- **专利相关的技术细节**：违反保密协议
- **个人信息**：学生证号、身份证号等
- **课题组未公开成果**：保护知识产权

### 安全实践

1. **数据脱敏**：输入前去掉文件名中的真实项目名称
2. **用模拟数据**：让 AI 帮你生成测试数据来调试代码
3. **本地部署**：敏感项目考虑用 Ollama 等本地模型
4. **企业版/团队版**：如果课题组统一订阅，注意选择不用于训练的版本
5. **联网检索类工具**（如 Perplexity、部分场景下的 Microsoft Copilot）：查询会经厂商服务器甚至对接网页检索，**切勿**粘贴未发表数据、课题内部资料；需要正式文献仍以数据库与图书馆检索为主

---

## 五、与各科研软件的配合方式

不同软件和 AI 的配合方式不同，核心思路如下：

| 软件 | AI配合方式 | 主要AI工具 |
|------|-----------|-----------|
| Origin | 对话式AI生成脚本 + Python接口 | Claude / DeepSeek / 通义 |
| MATLAB | 对话式AI生成.m代码 + 编辑器内AI辅助 | Claude + Cursor（或 JetBrains + 对话式 AI） |
| Excel | 对话式AI生成公式/VBA + Copilot | ChatGPT + Copilot；Office 场景可辅以 Microsoft Copilot |
| COMSOL | 对话式AI辅助建模思路 + Java API | Claude |
| FDTD | 对话式AI辅助脚本编写 | Claude / DeepSeek |
| SolidWorks | 对话式AI辅助建模思路 + 宏 | Claude |
| C4D | 对话式AI辅助 + Python脚本 | Claude |
| LabVIEW | 对话式AI辅助设计思路 | Claude / DeepSeek |

**通用模式**：先在对话式 AI 中描述需求、获取代码/思路，然后在软件中实现和验证。

---

## 下一步

选择你正在使用的工具，进入对应章节查看详细指南：

- [02 - Origin](02-origin.md)
- [03 - MATLAB](03-matlab.md)
- [04 - Excel](04-excel.md)
- [05 - COMSOL](05-comsol.md)
- [06 - FDTD](06-fdtd.md)
- [07 - SolidWorks](07-solidworks.md)
- [08 - C4D](08-c4d.md)
- [09 - LabVIEW](09-labview.md)
