# AI工具选择与使用指南

目前市面上的 AI 工具大致分三类：**对话式 AI**（问答、文档、图像、检索）、**编程辅助 AI**（嵌入编辑器或终端）和**Agent 工作流**（给定目标后自主规划、调用工具并验证）。本章帮你搞清楚用哪个、怎么用。

!!! info "价格与产品信息时效"

    **以下模型线、价格、免费额度与产品名称已于 2026 年 5 月 19 日核对**，厂商政策与定价变化频繁。订阅、选课或申请教育优惠前，**务必以各产品官网当日说明为准**；建议与 [课题组信息与本地约定](11-lab-info.md) 中的账号说明对照使用。

---

## 一、对话式AI对比

下表列出四款当前主流对话产品；更多国际与国内选择见本节 **「其他主流选择」**。

| 特性 | Claude | ChatGPT | DeepSeek | Gemini |
|------|--------|---------|----------|--------|
| **开发商** | Anthropic | OpenAI | DeepSeek | Google |
| **代表模型线** | Claude Opus 4.7 / Sonnet 4.6 | GPT-5.5 / GPT-5.5 Pro / GPT-5.5 Instant | DeepSeek V4-Pro / V4-Flash | Gemini 3.1 Pro / Flash-Lite |
| **强项** | 代码质量、长文本理解、深度推理、MCP 与 Claude Code 生态 | 通用能力、图像/语音/视频生态、Deep Research、Codex 编程工作流 | 中文友好、开源/开放权重、性价比高、本地部署选择多 | 长上下文、复杂推理、Google 生态、多模态 |
| **弱项** | 免费额度较紧，复杂任务成本较高 | 产品线变化快，旧模型会逐步退役 | Web/App/API 模型名与能力可能不同，需看官方文档 | 部分地区可用性与套餐差异较大，中文表达不如国产模型自然 |
| **免费额度** | 有（通常有限） | 有（以 ChatGPT 当日页面为准） | 有（较充裕） | 有（以 Gemini 当日页面为准） |
| **学生优惠** | 暂无 | ChatGPT Edu（部分学校） | 暂无 | 暂无 |
| **推荐场景** | 复杂代码生成、长论文分析、科研写作、Agent 开发 | 通用问答、多模态任务、深度研究、编程 Agent | 日常编程、代码调试、中文任务、本地部署 | 长文档分析、复杂图文理解、Google 生态用户 |

### 其他主流选择

下表补充常见国际与国内网页对话产品，可与上表四款搭配使用；能力边界与可用地区**以各产品官网为准**。

| 工具 | 类型 | 强项 | 注意 |
|------|------|------|------|
| **Grok**（xAI） | 国际 | 推理能力强（Grok-3）、实时信息获取、X/Twitter 集成 | 部分地区需 VPN；免费额度以官网为准 |
| **Perplexity** | 国际 | 检索增强、回答常附引用链接，适合快速查证与入门线索 | **不能替代**正式文献检索与数据库综述；联网场景注意第六节隐私 |
| **Microsoft Copilot** | 国际（网页/Windows/Edge） | 与 Microsoft 365、Edge、Windows、Office 生态深度集成 | 功能随系统版本与 Microsoft 365 等订阅变化，Copilot+PC 特性另见官网 |
| **GLM / 智谱清言（Z.ai）** | 国内常用 / 开放权重 | GLM-5.1 在长程 Agent、代码与中文工程任务上表现突出，可作为国产模型重点选择 | 以 [Z.ai 文档](https://docs.z.ai/guides/llm/glm-5.1) 与 [Hugging Face 模型页](https://huggingface.co/zai-org/GLM-5.1) 为准 |
| **Kimi**（月之暗面） | 国内常用 | 长文本、中文场景常见，K2 模型 | 额度与模型版本以 [kimi.moonshot.cn](https://kimi.moonshot.cn) 为准 |
| **通义千问（Qwen）** | 国内常用 | Qwen3 系列开源强大、阿里生态、工具调用、代码能力 | 以阿里云/通义官网能力与条款为准，开源版可本地部署 |
| **豆包（字节跳动）** | 国内常用 | 多模态、中文对话自然、与抖音/飞书等字节生态结合 | 以豆包官网能力与条款为准 |
| **元宝（腾讯）** | 国内常用 | 与微信/腾讯文档等腾讯生态集成、中文场景 | 以腾讯混元/元宝官网能力与条款为准 |

### 选择建议

- **写 MATLAB/Python 代码**：Claude（尤其 Claude Code）、ChatGPT/Codex、DeepSeek 都可用；复杂项目优先选择能读写文件并运行测试的 Agent 工具
- **需要深度推理（复杂公式推导、疑难 bug 分析）**：Claude 扩展思考、ChatGPT GPT-5.5 Thinking/Pro、Gemini 3.1 Pro、DeepSeek V4 思考模式、GLM-5.1 都值得交叉验证
- **处理中文文档/翻译**：DeepSeek、GLM-5.1 中文处理出色；也可结合 **通义千问**、**Kimi**、**豆包**
- **需要看图分析**：ChatGPT、Gemini 3.1 Pro、Claude Opus 4.7 都支持图像理解；涉及图表读数时仍需人工核对
- **长文档阅读（论文、综述）**：Gemini 3.1 Pro 和 Claude 都适合长文档；长中文材料可对比 **Kimi**
- **需要「带出处」的快速查证**：可考虑 **Perplexity**（仍须用正式数据库与综述核对）
- **已深度使用 Google / Microsoft / Apple 生态**：优先考虑 **Gemini**、**Microsoft Copilot** 或对应生态 AI
- **开源/本地部署需求**：DeepSeek V4、GLM-5.1、Qwen3、Llama 等开源/开放权重模型可搭配 Ollama、vLLM、SGLang 等本地工具
- **日常随手问**：哪个方便用哪个，差异不大
- **涉密、未发表数据、课题组未公开成果**：一律勿输入云端工具；见第六节

### 费用参考（2026年5月）

| 产品 | 免费版 | 付费版（月费） |
|------|--------|----------------|
| Claude | 有限免费（通常为 Sonnet 系列） | Pro 常见 $20/月；Max/Team/Enterprise 提供更多用量与管理能力 |
| ChatGPT | 有免费档 | Plus 常见 $20/月；Pro/Team/Edu/Enterprise 按场景选择 |
| DeepSeek | Web/App 常见免费或低门槛 | API 按量付费；官方模型名与旧别名会调整 |
| Gemini | 有免费档 | Google AI Pro / Ultra 或 Google One AI Premium 等套餐随地区变化 |

### 扩展工具费用速查

以下档位变化快，**仅列常见形态**；订阅前请以官网当日页面为准。

| 产品 | 说明（以官网为准） |
|------|-------------------|
| Grok | 常见为免费档 + SuperGrok 等付费档 |
| Perplexity | 常见为免费档 + Pro 等订阅档 |
| Microsoft Copilot | 免费能力与 Microsoft 365 订阅捆绑因地区与套餐而异 |
| GLM / 智谱清言 | GLM-5.1 API、Coding Plan、开放权重与第三方接入价格差异较大，以 Z.ai / 智谱官方说明为准 |
| Kimi | 额度与会员以 [kimi.moonshot.cn](https://kimi.moonshot.cn) 当日说明为准 |
| 通义千问 | 以阿里云/通义官网当日定价为准，开源版免费自部署 |
| 豆包 | 以豆包官网当日定价与额度为准 |
| 元宝 | 以腾讯混元/元宝官网当日定价与额度为准 |

> 建议：先用免费版熟悉，确认有持续需求再考虑付费。科研中 Claude Pro、ChatGPT Plus/Pro 或 Gemini 付费档的价值主要来自更强模型、更长上下文、更高额度和 Agent/深度研究能力。国内用户如 VPN 不便，DeepSeek V4、GLM-5.1、通义、Kimi、豆包等中文工具也能覆盖大量日常需求。

> **时效性说明**：各产品名称、定价与政策会随厂商调整而变化，请以官方网站当日公布为准；本手册中的价格与功能描述仅作参考，建议每学期核对一次。

---

## 二、AI编程工具对比

### 2.1 编辑器插件 / 独立 IDE

| 特性 | GitHub Copilot | Cursor | Windsurf |
|------|---------------|--------|----------|
| **形态** | VS Code/JetBrains 插件 | 独立IDE（基于VS Code） | 独立IDE |
| **核心功能** | 代码补全、Chat、Agent模式 | Tab补全、Composer、Agent模式、项目级理解 | 代码补全、Cascade（Agent）、多文件编辑 |
| **强项** | 与GitHub深度集成、稳定性好、生态最大 | Agent模式强、项目上下文理解深、MCP支持 | 上手快、Cascade流式体验好 |
| **弱项** | Agent模式相对保守 | 需迁移到新IDE、免费额度有限 | 生态较新 |
| **学生优惠** | 有（GitHub Education） | 暂无 | 暂无 |
| **适合谁** | 已有VS Code习惯、求稳的人 | 想要最强AI编码体验的人 | 想要轻量级Agent辅助的人 |

### 2.2 CLI 命令行工具（终端AI）

除 IDE 插件外，终端原生的 AI 编程工具已成为重要选择，尤其适合无 GUI 的服务器环境或习惯命令行的用户。

| 特性 | Claude Code | Codex CLI | GitHub Copilot CLI |
|------|------------|-----------|-------------------|
| **开发商** | Anthropic | OpenAI | GitHub |
| **形态** | 终端CLI | 终端CLI | 终端CLI（`gh copilot`） |
| **强项** | 项目级理解强、Agent自主执行、MCP原生支持 | 与 OpenAI / ChatGPT / Codex 生态结合，适合终端式代码任务 | 与GitHub/Git工作流结合 |
| **弱项** | 需Anthropic API或Max订阅 | 生态较新 | 功能比Claude Code精简 |
| **适合谁** | 复杂重构、多文件改动、无GUI环境 | OpenAI生态用户 | GitHub深度用户 |

> Claude Code 目前是终端 AI 编程的标杆产品，Agent 模式可自主完成「理解代码 → 修改 → 验证」闭环，适合大型重构或跨文件改动。

### 2.3 其他常见形态

不想换主编辑器、或惯用 JetBrains 时，可考虑下列形态；产品名与功能以官网为准。

| 工具 | 形态 | 适合谁 | 说明 |
|------|------|--------|------|
| **Codeium** | VS Code、JetBrains、Vim 等多编辑器插件 | 需要免费档较常见的补全/聊天、**不愿换 IDE** | 与 Copilot 类似偏「插件补全」，深度项目级能力因编辑器而异 |
| **JetBrains AI Assistant / Junie** | 内置于 IntelliJ IDEA、PyCharm 等 JetBrains IDE | **坚持用 JetBrains 栈**、不迁到 VS Code 的用户 | 具体功能名（如 Assistant、Junie）与订阅以 [jetbrains.com/ai](https://www.jetbrains.com/ai/) 为准 |
| **Amazon Q Developer** | AWS 工具链与多款 IDE 插件 | 深度使用 **AWS** 的开发者 | 与云资源、IAM 策略相关，以 AWS 官网说明为准 |

### 选择建议

- **MATLAB 编程**：Copilot 不直接支持 MATLAB；推荐用 Claude Code（终端）+ 对话式 Claude/DeepSeek；或用 Cursor + 对话式AI
- **Python/LabVIEW脚本**：Claude Code 或 Cursor 是最佳选择；仅要补全可选 Copilot 或 Codeium
- **VBA/Excel**：Copilot 和 Microsoft Copilot 支持较好；Claude/ChatGPT 对话也覆盖
- **日常多语言开发**：Cursor（Agent模式）和 Claude Code 最全面
- **不换编辑器、只要补全/Chat**：优先 GitHub Copilot、Codeium 等插件
- **服务器/无GUI环境**：Claude Code（终端）是唯一选择
- **云 API、数据出境或合规敏感**：与第六节「隐私与安全」、课题组规定结合，谨慎选择联网助手

### 费用参考

| 产品 | 个人版 | 学生版 |
|------|--------|--------|
| GitHub Copilot | $10/月（或含 GitHub 订阅） | 免费（GitHub Education） |
| Cursor | $20/月（Pro） | 暂无 |
| Windsurf | 有免费额度 | 暂无 |
| Claude Code | 需 API Key、Claude 订阅或团队/企业额度，具体以 Anthropic 页面为准 | 暂无明确通用学生档 |
| Codex CLI | 需 OpenAI API Key 或 ChatGPT/Codex 相关订阅，具体以 OpenAI 页面为准 | 以官网为准 |
| Codeium | 常见有免费档，团队/企业档见官网 | 见官网 |
| JetBrains AI | 常与 IDE 订阅或单独 AI 订阅绑定 | 见官网 |

> 强烈建议：先注册 GitHub Education（只需学校邮箱），免费获得 Copilot。

> 编程类工具的月费、学生政策同样可能变更，以各产品官网为准。

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
| 能力边界 | 只能输出文本 | 可读写文件、运行命令、搜索网络 |
| 典型场景 | "帮我写一段代码" | "帮我在项目中找到所有性能瓶颈并修复" |
| 代表产品 | ChatGPT / Claude / Gemini / DeepSeek 网页版 | Claude Code、Codex CLI、Cursor Agent、Windsurf Cascade、Manus、Devin |

### 3.3 对课题组的实用价值

- **代码与数据管理**：使用 Claude Code + MCP 文件系统，AI 可直接操作项目文件
- **文献管理**：MCP 连接 Zotero/文献库，AI 帮助整理、检索文献
- **数据安全**：MCP 可限制工具可访问的本地目录和动作，但如果连接的是云端模型，对话内容和必要上下文仍可能发送给服务商；涉密数据仍需本地模型或单位批准的企业方案
- **跨工具协作**：一次配置 MCP server，Claude Desktop、Cursor、Claude Code 均可使用

> **当前建议**：课题组同学可以先从 Claude Desktop + 文件系统 MCP 入手，体验「AI 直接读你的论文 PDF」的便利。进阶后使用 Claude Code 进行代码项目级辅助。

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

### GitHub Education（强烈推荐）

1. 访问 [education.github.com](https://education.github.com)
2. 用学校邮箱注册/登录 GitHub
3. 上传学生证明（学生证照片或学信网截图）
4. 审核通过后，在权益页面激活 Copilot

### Claude

1. 访问 [claude.ai](https://claude.ai)
2. 注册账号（可用 Google 登录）
3. 免费版、Pro、Max、Team 等档位可用模型和额度以页面当日说明为准；复杂科研任务优先尝试 Opus/Sonnet 的思考模式
4. **Claude Code**：终端安装与登录方式以 Anthropic 官方说明为准，适合多文件项目和批量脚本维护

### ChatGPT

1. 访问 [chat.openai.com](https://chat.openai.com)
2. 注册账号
3. 免费版、Plus、Pro、Team/Edu/Enterprise 的模型和额度会变化；复杂任务优先尝试 GPT-5.5、Deep Research 或 Codex 相关能力

### DeepSeek

1. 访问 [chat.deepseek.com](https://chat.deepseek.com)
2. 注册账号
3. Web/App 与 API 的模型名可能不同；截至本次核对，官方 API 文档已进入 V4 Preview 线（V4-Pro / V4-Flash），并提示旧 `deepseek-chat` / `deepseek-reasoner` 别名会调整

### GLM / 智谱清言（Z.ai）

1. 访问 [chatglm.cn](https://chatglm.cn) 或 Z.ai 相关入口，按页面指引注册
2. 若用于代码 Agent，可重点关注 GLM-5.1、GLM Coding Plan、OpenAI 兼容 API 或第三方接入方式
3. GLM-5.1 是文本模型，长程工程任务和代码场景表现较强；涉及图像、多模态或极长文档时需与其他模型搭配

### Grok

1. 访问 [grok.xai.com](https://grok.xai.com)（若所在地区入口不同，以 xAI 官方说明为准）
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

### Codeium

1. 访问 [codeium.com](https://codeium.com)
2. 注册账号后在目标编辑器中安装 Codeium 插件并按向导登录
3. 免费与团队政策以官网为准

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
3. **本地部署**：敏感项目考虑用 Ollama + DeepSeek V4、GLM-5.1、Qwen3 等开源/开放权重模型本地运行
4. **MCP 本地连接**：使用 Claude Desktop、Cursor 或 Claude Code 的文件系统 MCP 连接，让 AI 在授权范围内读取本地文件；若模型在云端，对话内容和必要上下文仍经 API
5. **企业版/团队版**：如果课题组统一订阅，注意选择不用于训练的版本（如 ChatGPT Team、Claude Team）
6. **联网检索类工具**（如 Perplexity、部分场景下的 Microsoft Copilot）：查询会经厂商服务器甚至对接网页检索，**切勿**粘贴未发表数据、课题内部资料；需要正式文献仍以数据库与图书馆检索为主

---

## 七、与各科研软件的配合方式

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
| LabVIEW | 对话式AI辅助设计思路 | Claude / DeepSeek |

**通用模式**：先在对话式 AI 中描述需求、获取代码/思路，然后在软件中实现和验证。

---

## 八、本次核对来源

以下链接用于核对 2026-05-19 更新中的主要趋势和模型线。产品可用性、模型名称、价格和额度仍以官网当日页面为准。

- [Stanford HAI 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report%C2%A0)：用于把握 AI 投资、能力、治理和科研应用趋势。
- [OpenAI GPT-5.5 announcement](https://openai.com/index/introducing-gpt-5-5/) 与 [GPT-5.5 Instant announcement](https://openai.com/index/gpt-5-5-instant/)：用于核对 OpenAI GPT-5.5 公开模型线。
- [Anthropic Claude Opus 4.7 announcement](https://www.anthropic.com/news/claude-opus-4-7)：用于核对 Claude Opus 4.7、Agent/编码和高分辨率视觉能力。
- [Google Gemini 3.1 Pro announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/) 与 [Gemini 3.1 Pro model card](https://deepmind.google/models/model-cards/gemini-3-1-pro)：用于核对 Gemini 3.1 Pro。
- [DeepSeek V4 Preview release](https://api-docs.deepseek.com/news/news260424)、[DeepSeek API change log](https://api-docs.deepseek.com/updates/) 与 [DeepSeek transparency center](https://www.deepseek.com/en/transparency/)：用于核对 DeepSeek V4 线、模型发布和旧 API 别名调整。
- [Z.ai GLM-5.1 documentation](https://docs.z.ai/guides/llm/glm-5.1) 与 [GLM-5.1 Hugging Face model page](https://huggingface.co/zai-org/GLM-5.1)：用于核对 GLM-5.1 的定位、上下文和开放权重信息。

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
