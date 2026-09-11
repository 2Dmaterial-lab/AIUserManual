# AI工具选择与使用指南

目前市面上的 AI 工具大致分三类：**对话式 AI**（问答、文档、图像、检索）、**编程辅助 AI**（嵌入编辑器或终端）和**Agent 工作流**（给定目标后自主规划、调用工具并验证）。本章帮你搞清楚用哪个、怎么用。

!!! info "价格与产品信息时效"

    **本章于 2026 年 9 月 11 日核对主要模型目录、工具入口与教育权益**，厂商政策与定价变化频繁。订阅、选课或申请教育优惠前，**务必以各产品官网当日说明为准**；建议与 [课题组信息与本地约定](11-lab-info.md) 中的账号说明对照使用。

---

## 一、对话式AI对比

下表列出四类常用产品。**网页/App、API 和编程工具的可用模型可能不同**；代表模型来自官方目录，不表示免费账号或所有地区都能使用。更多选择见「其他主流选择」。

| 特性 | Claude | ChatGPT | DeepSeek | Gemini |
|------|--------|---------|----------|--------|
| **开发商** | Anthropic | OpenAI | DeepSeek | Google |
| **代表模型线** | Claude Fable 5.1 / Opus 5 / Sonnet 5 / Haiku 4.5 [1](#source-1) | GPT-6 Astra / GPT-5.6 系列 [2](#source-2) | DeepSeek V4-Pro / V4-Flash（正式版）[3](#source-3) | Gemini 3.8 Flash / 3.5 Flash-Lite；3.1 Pro 为 API Preview [4](#source-4) |
| **强项** | 代码质量、长文本理解、深度推理、MCP 与 Claude Code 生态 | 通用能力、图像/语音/视频生态、Deep Research、Codex 编程工作流 | 中文友好、开源/开放权重、性价比高、本地部署选择多 | 长上下文、复杂推理、Google 生态、多模态 |
| **使用前确认** | 模型权限、用量与费用 | 当前客户端、套餐与工作区开放的模型 | Web/App/API 能力与计费差异 | App 与 API 型号不同；稳定版与 Preview 分开选择 |
| **额度** | 以账号用量页为准 | 以账号用量页为准 | 网页使用与 API 余额分别查看 | 以账号及地区为准 |
| **教育使用** | 查看学校采购或官方教育项目 | Edu 属于学校方案，不能等同个人学生折扣 | 查看官网活动与学校安排 | 查看所在地区的教育活动与资格 |
| **适用场景** | 复杂代码生成、长论文分析、科研写作、Agent 开发 | 通用问答、多模态任务、深度研究、编程 Agent | 日常编程、代码调试、中文任务、本地部署 | 长文档分析、复杂图文理解、Google 生态用户 |

### 其他主流选择

下表补充常见国际与国内网页对话产品，可与上表四款搭配使用；能力边界与可用地区**以各产品官网为准**。

| 工具 | 类型 | 强项 | 注意 |
|------|------|------|------|
| **Grok**（xAI） | 国际 | 实时信息检索、推理与 X 内容相关任务 | 使用 [Grok 官方入口](https://grok.com/)，核对地区与账号可用性 |
| **Perplexity** | 国际 | 检索增强、回答常附引用链接，适合快速查证与入门线索 | **不能替代**正式文献检索与数据库综述；联网场景注意第六节隐私 |
| **Microsoft Copilot** | 国际（网页/Windows/Edge） | 与 Microsoft 365、Edge、Windows、Office 生态深度集成 | 功能随系统版本与 Microsoft 365 等订阅变化，Copilot+PC 特性另见官网 |
| **GLM / 智谱清言（Z.ai）** | 国内常用 / 开放权重 | 中文、代码与 Agent 任务；具体型号按官方目录选择 | 以 [Z.ai 模型目录](https://docs.z.ai/guides/overview/overview) 为准；开放权重与托管 API 分别核对 |
| **Kimi**（月之暗面） | 国内常用 | 长文本、中文资料与代码任务；型号见 [Kimi 官方目录](https://platform.kimi.ai/docs/overview) | 额度与模型版本以 [kimi.moonshot.cn](https://kimi.moonshot.cn) 为准 |
| **通义千问（Qwen）** | 国内常用 | Qwen 系列开放模型、阿里生态、工具调用与代码能力 | 以阿里云/通义官网能力与条款为准，开源版可本地部署 |
| **豆包（字节跳动）** | 国内常用 | 多模态、中文对话自然、与抖音/飞书等字节生态结合 | 以豆包官网能力与条款为准 |
| **元宝（腾讯）** | 国内常用 | 与微信/腾讯文档等腾讯生态集成、中文场景 | 以腾讯混元/元宝官网能力与条款为准 |

### 选择参考

- **写 MATLAB/Python 代码**：Claude Code、ChatGPT/Codex、DeepSeek 都可用；复杂项目可选择能读写文件并运行测试的 Agent 工具
- **需要深度推理（复杂公式推导、疑难 bug 分析）**：Claude 扩展思考、ChatGPT 当前可用的推理模型、Gemini 推理模型、DeepSeek V4 思考模式、GLM 都值得交叉验证
- **处理中文文档/翻译**：DeepSeek、GLM 可用于中文处理；也可结合 **通义千问**、**Kimi**、**豆包**
- **需要看图分析**：ChatGPT、Gemini、Claude 中选择支持视觉的模型；涉及图表读数时仍需人工核对
- **长文档阅读（论文、综述）**：Gemini 和 Claude 都适合长文档；长中文材料可对比 **Kimi**
- **需要「带出处」的快速查证**：可考虑 **Perplexity**（仍须用正式数据库与综述核对）
- **已深度使用 Google / Microsoft / Apple 生态**：可考虑 **Gemini**、**Microsoft Copilot** 或对应生态 AI
- **开源/本地部署需求**：先按显存、内存和许可证选择较小的开放权重模型，再核对 Ollama、vLLM 或 SGLang 的支持清单；大型模型不能假定普通电脑可运行
- **日常随手问**：哪个方便用哪个，差异不大
- **涉密、未发表数据、课题组未公开成果**：一律勿输入云端工具；见第六节

### 费用与套餐（2026年9月核对）

**网页订阅通常不等于 API 额度**。批量分析、Agent 长任务和联网工具可能有独立用量限制；先做小样本，查看实际消耗，再决定套餐。这里保留官方费用入口，不把短期价格写成长期承诺。

| 产品 | 订阅与 API 的区别 | 核对入口 |
|------|------------------|----------|
| Claude | 网页套餐、Claude Code 使用方式与 Console API 计费分别确认 | [官方套餐](https://claude.com/pricing) |
| ChatGPT / Codex | 免费、个人、Business、Edu/Enterprise 与 API 使用范围不同；以账号实际权益为准 | [ChatGPT 定价](https://chatgpt.com/pricing)、[Codex 费用与用量](https://developers.openai.com/codex/pricing) |
| DeepSeek | Web/App 与 API 分开；V4 API 已引入峰谷时段计费，输入缓存与输出分别计费 | [API 定价](https://api-docs.deepseek.com/quick_start/pricing/) |
| Gemini | Google AI 订阅与 Gemini API 分开；地区、模型和 Preview 状态会影响可用性 | [Google AI 套餐](https://one.google.com/about/google-ai-plans/)、[API 定价](https://ai.google.dev/gemini-api/docs/pricing) |

### 扩展工具费用速查

以下档位变化快，**仅列常见形态**；订阅前请以官网当日页面为准。

| 产品 | 说明（以官网为准） |
|------|-------------------|
| Grok | 常见为免费档 + SuperGrok 等付费档 |
| Perplexity | 常见为免费档 + Pro 等订阅档 |
| Microsoft Copilot | 免费能力与 Microsoft 365 订阅捆绑因地区与套餐而异 |
| GLM / 智谱清言 | GLM API、Coding Plan、开放权重与第三方接入价格差异较大，以 Z.ai / 智谱官方说明为准 |
| Kimi | 额度与会员以 [kimi.moonshot.cn](https://kimi.moonshot.cn) 当日说明为准 |
| 通义千问 | 以阿里云/通义官网当日定价为准，开放模型自部署仍有硬件、运维成本，并受模型许可证约束 |
| 豆包 | 以豆包官网当日定价与额度为准 |
| 元宝 | 以腾讯混元/元宝官网当日定价与额度为准 |

> 建议：先用免费版熟悉，确认有持续需求再考虑付费。Claude Pro、ChatGPT Plus/Pro 或 Gemini 付费档的主要差异通常在模型权限、上下文长度、额度和 Agent/深度研究能力。按所在地允许的服务与学校安排选择；DeepSeek、GLM、通义、Kimi、豆包等也可用于日常任务。

> **时效性说明**：各产品名称、定价与政策会随厂商调整而变化，请以官方网站当日公布为准；本手册中的价格与功能描述仅作参考，建议每学期核对一次。

---

## 二、AI编程工具对比

### 2.1 编辑器插件 / 独立 IDE

| 特性 | GitHub Copilot | Cursor | Windsurf |
|------|---------------|--------|----------|
| **形态** | VS Code/JetBrains 插件 | 独立IDE（基于VS Code） | 独立IDE |
| **核心功能** | 代码补全、Chat、Agent模式 | Tab补全、Composer、Agent模式、项目级理解 | 代码补全、Cascade（Agent）、多文件编辑 |
| **强项** | 与 GitHub、受支持编辑器和代码审查工作流集成 | Agent模式强、项目上下文理解深、MCP支持 | 上手快、Cascade流式体验好 |
| **使用前确认** | 编辑器、Agent 功能和额度 | 项目权限、模型消耗与云端任务范围 | Editor 与旧插件的功能和维护状态 |
| **学生权益** | 以已验证学生的权益页为准 [5](#source-5) | 官方学生页介绍校园/线上活动优惠 [6](#source-6) | 以官网当期教育活动为准 |
| **适合谁** | 已有 VS Code 习惯、希望保留原编辑器的人 | 需要项目级上下文和 Agent 工作流的人 | 需要轻量级 Agent 辅助的人 |

### 2.2 CLI 命令行工具（终端AI）

除 IDE 插件外，终端原生的 AI 编程工具已成为重要选择，尤其适合无 GUI 的服务器环境或习惯命令行的用户。

| 特性 | Claude Code | Codex CLI | GitHub Copilot CLI |
|------|------------|-----------|-------------------|
| **开发商** | Anthropic | OpenAI | GitHub |
| **形态** | 终端CLI | 终端CLI | 独立终端 CLI（`copilot`）[7](#source-7) |
| **强项** | 项目级理解强、Agent自主执行、MCP原生支持 | 与 OpenAI / ChatGPT / Codex 生态结合，适合终端式代码任务 | 与GitHub/Git工作流结合 |
| **使用前确认** | 套餐额度与 API 计费方式 | 登录方式、模型权限与执行环境 | 当前 Copilot 计划和工具权限 |
| **适合谁** | 复杂重构、多文件改动、无GUI环境 | OpenAI生态用户 | GitHub深度用户 |

> Claude Code 是终端 AI 编程工具中的常见选择，Agent 模式可自主完成「理解代码 → 修改 → 验证」闭环，适合跨文件改动和批量脚本维护。

**旧教程迁移**：`gh copilot` 扩展已退役。新用户应按 [GitHub 官方安装指南](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli) 安装独立 Copilot CLI，不再沿用旧扩展安装命令。

### 2.3 桌面应用与其他常见形态

不想换主编辑器、或惯用 JetBrains 时，可考虑下列形态；产品名与功能以官网为准。

| 工具 | 形态 | 适合谁 | 说明 |
|------|------|--------|------|
| **Windsurf Plugins（原 Codeium）** | 多编辑器插件 | 维护既有插件环境的用户 | 多个旧插件已处于维护模式；新项目先看 [官方维护状态](https://docs.windsurf.com/plugins/getting-started)，尤其注意 JetBrains 迁移说明 [8](#source-8) |
| **Codex 桌面应用 / IDE 扩展** | 桌面任务、项目文件与编辑器内工作流 | 希望直接整理文件、分析数据或维护仓库的用户 | 先确认工作目录、已连接应用和验收标准；具体功能以 [官方文档](https://developers.openai.com/codex/app) 为准 |
| **JetBrains AI Assistant / Junie** | 内置于 IntelliJ IDEA、PyCharm 等 JetBrains IDE | **坚持用 JetBrains 栈**、不迁到 VS Code 的用户 | 具体功能名（如 Assistant、Junie）与订阅以 [jetbrains.com/ai](https://www.jetbrains.com/ai/) 为准 |
| **Amazon Q Developer** | AWS 工具链与多款 IDE 插件 | 深度使用 **AWS** 的开发者 | 与云资源、IAM 策略相关，以 AWS 官网说明为准 |

### 选择参考

- **MATLAB 编程**：MATLAB 内置的 **MATLAB Copilot** 与 **GitHub Copilot** 是不同产品；前者需满足 MathWorks 版本、地区与许可要求，后者可在受支持编辑器中辅助 `.m` 文件；也可用 Claude Code/Codex/Cursor 编写后在 MATLAB 中运行 [9](#source-9)
- **Python/LabVIEW脚本**：Claude Code、Cursor 都可处理项目级脚本；仅要补全可选 Copilot 或受支持的 Windsurf 插件
- **VBA/Excel**：Copilot 和 Microsoft Copilot 支持较好；Claude/ChatGPT 对话也覆盖
- **日常多语言开发**：Cursor（Agent模式）和 Claude Code 覆盖面较广
- **不换编辑器、只要补全/Chat**：可考虑 GitHub Copilot 等仍支持当前编辑器版本的插件
- **服务器/无 GUI 环境**：可考虑 Claude Code、Codex CLI 等终端工具
- **云 API、数据出境或合规敏感**：与第六节「隐私与安全」、课题组规定结合，谨慎选择联网助手

### 费用参考

| 产品 | 费用/权益核对入口 | 选择时看什么 |
|------|--------------------|--------------|
| GitHub Copilot | [官方计划](https://docs.github.com/en/copilot/get-started/plans) | 免费与付费计划、AI 用量；学生权益需要验证资格 |
| Cursor | [定价](https://cursor.com/pricing)、[学生页](https://cursor.com/students) | Agent 用量与超额费用；校园活动不能视为所有学生自动获赠订阅 |
| Windsurf | [定价](https://windsurf.com/pricing) | Editor、插件与团队计划分别核对 |
| Claude Code | [官方使用与订阅说明](https://code.claude.com/docs/en/overview) | 订阅登录和 API 按量付费不同 |
| Codex | [官方费用与用量](https://developers.openai.com/codex/pricing) | ChatGPT 登录与 API Key 登录的计费方式不同 |
| JetBrains AI | [官方产品页](https://www.jetbrains.com/ai/) | IDE 版本、AI Assistant/Junie 与账号权益 |

> 有学校邮箱不代表自动获得全部教育权益。申请前查看资格、所在地区和有效期；不要把付费网页订阅理解为无限 API 或无限 Agent 使用量。

---

## 三、MCP协议与AI智能体（Agent）

### 3.1 什么是 MCP？

**MCP（Model Context Protocol，模型上下文协议）** 是由 Anthropic 于 2024 年底发布、并被多类 AI 工具采用的开放协议。它让 AI 模型能够**以标准方式连接外部工具和数据源**，例如本地文件、数据库、浏览器、文献管理器和实验数据目录。

对于科研工作者，MCP 的实际意义是：

- AI 可以直接**读取你电脑上的文件**（代码、数据、论文），而不需要你复制粘贴
- AI 可以**查询数据库、搜索网页、调用 API**
- 一次配置后，多个支持 MCP 的 AI 工具可复用相似的工具连接

### 3.2 什么是 AI Agent（智能体）？

传统对话式 AI 是「你问它答」，Agent 则是**能自主执行多步任务的 AI**：

| 模式 | 传统对话 | Agent 模式 |
|------|---------|-----------|
| 交互方式 | 一问一答 | 给定目标，自主规划并执行 |
| 能力边界 | 取决于所选模式，也可能支持附件、联网和分析工具 | 在授权工具与环境范围内执行多步任务 |
| 典型场景 | "帮我写一段代码" | "帮我在项目中找到所有性能瓶颈并修复" |
| 典型入口 | 各产品的普通问答模式 | Claude Code、Codex、Cursor Agent 等；部分网页产品也提供 Agent 模式 |

### 3.3 对课题组的实用价值

- **代码与数据管理**：Claude Code、Codex 等可通过自身文件工具操作项目；只有需要额外数据源时才配置 MCP
- **文献管理**：MCP 连接 Zotero/文献库，AI 帮助整理、检索文献
- **数据安全**：MCP 可限制工具可访问的本地目录和动作，但如果连接的是云端模型，对话内容和必要上下文仍可能发送给服务商；涉密数据仍需本地模型或单位批准的企业方案
- **跨工具协作**：可在支持 MCP 的不同客户端中配置同一服务；认证、传输方式和权限仍须逐个客户端核对

> **入门建议**：先用一份公开论文或示例数据完成任务。附件、已有文件工具或连接器能满足需求时，直接使用；需要扩展能力时再配置 MCP。MCP 本身不保证 PDF 解析、联网隔离或结果正确。

---

## 四、科研工作流建议

### 4.1 文献检索与综述

AI 可以用来**形成检索式、提炼问题、对比观点、整理笔记**，但不能替代正式文献检索。推荐流程：

1. 用 AI 把研究问题拆成关键词、同义词、材料体系、表征方法和应用场景。
2. 在 Web of Science、Scopus、Google Scholar、CNKI、arXiv、期刊官网等正式来源检索。
3. 把论文标题、摘要、DOI 和你关心的问题交给 AI 做初筛与表格化整理。
4. 对关键结论回到原文核对，尤其是实验条件、样品制备、表征参数和统计口径。

!!! warning "不要让 AI 编造引用"

    论文引用必须来自真实数据库或期刊官网。AI 给出的 DOI、页码、期刊名和作者列表都需要逐条核对。

### 4.2 数据分析与代码

- 让 AI 写脚本时，要求它同时给出**输入数据假设、异常值处理、单位说明、可复现实验步骤**。
- 对关键脚本保留版本号、运行环境、依赖包版本和随机种子。
- 让 Agent 改代码时，先限定工作目录和目标文件，完成后必须运行最小验证：小样本数据、极限情况、已知答案或图像肉眼检查。
- 对论文级图表，要求 AI 输出可重复运行的 MATLAB/Python 脚本，而不是只给操作步骤。

### 4.3 仿真与实验设计

- COMSOL、FDTD、SolidWorks、LabVIEW 等场景中，AI 适合生成脚本、解释报错、提出排查路径。
- 边界条件、网格无关性、材料参数、仪器量程、采样率、噪声模型等必须由研究者核对。
- 如果 AI 建议修改物理模型，要求它说明假设、适用范围和可能失效的情况。

### 4.4 论文写作与科研诚信

- AI 可以润色语言、检查逻辑、生成图注初稿、整理审稿回复框架。
- 论文核心创新、实验结果解释、结论边界必须由作者负责。
- 建议在项目记录中保留 AI 辅助痕迹：使用工具、日期、用途、是否用于正文或代码。
- 投稿前查看目标期刊、学校和课题组对 AI 使用声明的要求。

---

## 五、账号注册快速指南

### GitHub Education

1. 访问 [education.github.com](https://education.github.com)
2. 用学校邮箱注册/登录 GitHub
3. 按官方申请页面要求提交在读证明；不要把身份证件发给 AI 助手
4. 审核通过后，在权益页面确认并激活当前可用的 Copilot 学生权益 [5](#source-5)

### Claude

1. 访问 [claude.ai](https://claude.ai)
2. 注册账号（可用 Google 登录）
3. 免费版、Pro、Max、Team 等档位可用模型和额度以页面当日说明为准；复杂科研任务可尝试 Opus/Sonnet 的思考模式
4. **Claude Code**：按 [官方入门页](https://code.claude.com/docs/en/overview) 安装并选择登录方式；订阅额度与 Console API 账单分别核对

### ChatGPT

1. 访问 [chatgpt.com](https://chatgpt.com)
2. 注册账号
3. 免费版、Plus、Pro、Business/Edu/Enterprise 的模型和额度会变化；复杂任务使用账号可用的推理、Deep Research 或 Codex 能力

### DeepSeek

1. 访问 [chat.deepseek.com](https://chat.deepseek.com)
2. 注册账号
3. Web/App 与 API 的模型名可能不同；V4-Pro 已于 2026-08-13 正式发布。新脚本按官方目录使用 `deepseek-v4-pro` / `deepseek-v4-flash`，旧教程中的别名先核对再迁移 [3](#source-3)

### GLM / 智谱清言（Z.ai）

1. 访问 [chatglm.cn](https://chatglm.cn) 或 Z.ai 相关入口，按页面指引注册
2. 若用于代码 Agent，先查看官方模型目录、GLM Coding Plan、兼容 API 与账号支持的型号
3. 逐个型号确认是否支持图像、工具调用和所需上下文，不要把模型家族名当成统一能力保证

### Grok

1. 访问 [grok.com](https://grok.com/)（若所在地区入口不同，以 xAI 官方说明为准）
2. 使用 X/Twitter 或 Google 账号登录
3. 免费档与 SuperGrok 付费档以页面当日说明为准

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

### Windsurf Plugins（原 Codeium）

1. 访问 [官方插件文档](https://docs.windsurf.com/plugins/getting-started)
2. 先查看目标编辑器的维护或弃用状态，再选择当前支持的插件或迁移路径
3. 根据官方向导安装、登录并核对用量 [8](#source-8)

### JetBrains AI

1. 打开 JetBrains IDE，在 **Plugins** 中搜索 **AI Assistant** 等官方 AI 插件，或访问 [jetbrains.com/ai](https://www.jetbrains.com/ai/)
2. 使用 JetBrains Account 登录并按向导启用
3. 试用、订阅与功能名以官网当日说明为准

### 豆包

1. 访问 [doubao.com](https://www.doubao.com) 或下载豆包 App
2. 使用手机号/抖音/飞书等账号登录
3. 额度与会员政策以官网当日说明为准

### 元宝

1. 访问 [yuanbao.tencent.com](https://yuanbao.tencent.com) 或下载元宝 App
2. 使用微信/QQ/手机号等账号登录
3. 额度与会员政策以官网当日说明为准

---

## 六、隐私与安全

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
3. **本地部署**：先用公开样例验证适合本机硬件的开放模型；确认推理、嵌入、OCR、日志和工具均在获准环境内处理，再按课题组规定使用
4. **MCP 本地连接**：使用 Claude Desktop、Cursor 或 Claude Code 的文件系统 MCP 连接，让 AI 在授权范围内读取本地文件；若模型在云端，对话内容和必要上下文仍经 API
5. **企业版/团队版**：如果课题组统一订阅，注意选择不用于训练的版本（如 ChatGPT Business、Claude Team）
6. **联网检索类工具**（如 Perplexity、部分场景下的 Microsoft Copilot）：查询会经厂商服务器甚至对接网页检索，**切勿**粘贴未发表数据、课题内部资料；需要正式文献仍以数据库与图书馆检索为主

---

## 七、科研软件工具选择速查 {: #tool-choice }

很多时候，真正的问题不是“这个软件能不能做”，而是“这件事应该优先用哪个工具做”。下表给出课题组日常任务的保守选择。

| 任务 | 首选 | 备选 | 不建议 |
|------|------|------|--------|
| 快速查看小规模实验数据 | Origin / Excel | MATLAB | 直接用截图记录结论 |
| 批量处理多文件数据 | MATLAB / Python | Excel VBA / Origin Python | 手动复制粘贴 |
| 论文级可复现出图 | MATLAB / Python / Origin 脚本 | Origin 模板 | 只保存 `.opju` 或截图 |
| 复杂公式、拟合、信号处理 | MATLAB | Python / Origin | Excel 手工公式堆叠 |
| 表格整理和临时报表 | Excel | Origin / Python | MATLAB 处理复杂格式表格 |
| 多物理场仿真 | COMSOL | MATLAB 自写简化模型 | 只靠 AI 判断物理模型 |
| 光子器件 FDTD 仿真 | Ansys Lumerical FDTD | COMSOL 波动光学 / Tidy3D 等 | 手动逐个参数点截图 |
| 机械结构设计和加工图 | SolidWorks | Fusion / FreeCAD | C4D 做加工件 |
| 科研三维示意图和动画 | C4D / Blender | SolidWorks 渲染 | 用示意图冒充仿真数据 |
| 仪器控制和自动采集 | LabVIEW / Python | MATLAB | 手动记录长期数据 |

### 推荐工作流

| 场景 | 建议流程 |
|------|----------|
| 实验数据到论文图 | Excel/Origin 快速预览 → MATLAB/Python 脚本正式处理 → Origin/C4D/Illustrator 做必要排版 → 保存源数据和脚本 |
| 仿真参数扫描 | GUI 建立基准模型 → 脚本/API 扫参数 → 导出 CSV/MAT → MATLAB/Python 统计和出图 |
| 仪器自动化 | 手动确认仪器命令 → LabVIEW/Python 做最小采集 → 加入异常处理和元数据保存 → 长时间测试 |
| 机械设计到加工 | 手绘需求和约束 → SolidWorks 参数化建模 → 工程图标注 → 人工复核材料、公差和加工方式 |
| 科研可视化 | 仿真/实验数据确定结构和比例 → C4D/Blender 制作示意图 → 图注说明比例、色标和数据来源 |

### AI 配合方式分层

| 层级 | 适合做什么 | 注意事项 |
|------|------------|----------|
| 对话式 AI | 选工具、写提示词、生成脚本、解释报错、检查逻辑 | 不能直接相信物理结论和引用 |
| 编辑器/Agent | 多文件脚本、批量处理、自动运行测试、重构项目 | 限定目录，要求它报告改动和验证 |
| 软件内置 AI | Excel Copilot、MATLAB Copilot、NI Nigel 等场景内辅助 | 能力随许可证变化，结果仍要人工验收 |
| 软件 API/宏 | Origin Python、MATLAB、COMSOL Java API、FDTD Script、VBA、C4D Python | 最适合可复现自动化，但需要小样本测试 |

## 八、与各科研软件的配合方式

不同软件和 AI 的配合方式不同，核心思路如下：

| 软件 | AI配合方式 | 主要AI工具 |
|------|-----------|-----------|
| Origin | 对话式AI生成脚本 + Python接口 | Claude / DeepSeek / 通义 |
| MATLAB | 对话式AI生成.m代码 + Agent/编辑器辅助 | Claude Code / Codex CLI / Cursor + 对话式 AI |
| Excel | 对话式AI生成公式/VBA + Copilot | ChatGPT + Copilot；Office 场景可辅以 Microsoft Copilot |
| COMSOL | 对话式AI辅助建模思路 + Java API | Claude |
| FDTD | 对话式AI辅助脚本编写 | Claude / DeepSeek |
| SolidWorks | 对话式AI辅助建模思路 + 宏 | Claude |
| C4D | 对话式AI辅助 + Python脚本 | Claude |
| LabVIEW | 对话式AI辅助设计思路 + 仪器命令/伪代码 | Claude / DeepSeek / NI Nigel AI（如可用） |

**通用模式**：先在对话式 AI 中描述需求、获取代码/思路，然后在软件中实现和验证。

---

## 九、本次核对来源

**核对日期：2026-09-11。** 下列目录用于查证产品状态，不是能力排名。优先选择能完成自己样例任务的工具；实验中记录实际模型 ID、日期、提示词、工具版本与结果验证方式。

| 编号 | 官方来源 | 本次更新依据 |
|------|----------|--------------|
| <span id="source-1">[1]</span> | [Claude 模型目录](https://platform.claude.com/docs/en/models/overview) | Fable 5.1、Opus 5、Sonnet 5、Haiku 4.5；API 与网页可用性分开核对 |
| <span id="source-2">[2]</span> | [OpenAI 模型与选择说明](https://developers.openai.com/codex/models) | GPT-6 Astra、GPT-5.6 Sol/Terra/Luna；权限取决于计划、客户端和开放范围 |
| <span id="source-3">[3]</span> | [DeepSeek V4-Pro 正式发布](https://api-docs.deepseek.com/news/news260813/)、[当前定价](https://api-docs.deepseek.com/quick_start/pricing/) | 8 月正式版与 8 月 16 日起峰谷计费；不再笼统标为 Preview |
| <span id="source-4">[4]</span> | [Gemini API 模型目录](https://ai.google.dev/gemini-api/docs/models) | 3.8 Flash、3.5 Flash-Lite 为稳定版；3.1 Pro 仍标为 Preview |
| <span id="source-5">[5]</span> | [GitHub Copilot 计划](https://docs.github.com/en/copilot/get-started/plans) | 当前计划与经过验证的学生权益 |
| <span id="source-6">[6]</span> | [Cursor 学生项目](https://cursor.com/students) | 以校园/线上活动和官方资格说明为准 |
| <span id="source-7">[7]</span> | [GitHub 旧 CLI 扩展退役说明](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli) | 从 `gh copilot` 迁移至独立 Copilot CLI |
| <span id="source-8">[8]</span> | [Windsurf 插件文档](https://docs.windsurf.com/plugins/getting-started) | 原 Codeium 名称与旧插件维护/迁移状态 |
| <span id="source-9">[9]</span> | [MATLAB Copilot 要求](https://www.mathworks.com/support/requirements/matlab-copilot.html) | 版本、登录、网络和地区条件；与 GitHub Copilot 区分 |

其他模型目录：[Z.ai](https://docs.z.ai/guides/overview/overview)、[Kimi](https://platform.kimi.ai/docs/overview)。未逐一验证的学校采购、内部账号和地区权益，应由使用者或课题组管理员确认。

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
