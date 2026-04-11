# AI工具选择与使用指南

目前市面上的 AI 工具大致分两类：**对话式 AI**（你问它答）和**编程辅助 AI**（嵌入编辑器实时辅助）。本章帮你搞清楚用哪个、怎么用。

!!! info "价格与产品信息时效"

    **以下价格、免费额度与产品名称已于 2026 年 4 月核对**，厂商政策与定价变化频繁。订阅、选课或申请教育优惠前，**务必以各产品官网当日说明为准**；建议与 [课题组信息与本地约定](11-lab-info.md) 中的账号说明对照使用。

---

## 一、对话式AI对比

| 特性 | Claude | ChatGPT | DeepSeek |
|------|--------|---------|----------|
| **开发商** | Anthropic | OpenAI | DeepSeek |
| **强项** | 长文本理解、代码质量、遵循指令 | 生态最全、插件丰富、GPT-4o多模态 | 代码能力强、中文理解好、性价比高 |
| **弱项** | 插件生态不如ChatGPT | 代码有时"自信地犯错" | 创意写作和复杂推理稍弱 |
| **免费额度** | 有（有限） | 有（GPT-4o mini） | 有（较充裕） |
| **学生优惠** | 暂无 | ChatGPT Edu（部分学校） | 暂无 |
| **推荐场景** | 代码生成、长文档分析、科研写作 | 通用问答、多模态任务、插件调用 | 日常编程、代码调试、中文任务 |

### 选择建议

- **写 MATLAB/Python 代码**：Claude 和 DeepSeek 都不错，Claude 在复杂逻辑上更稳
- **处理中文文档/翻译**：DeepSeek 中文处理出色
- **需要看图分析**：ChatGPT (GPT-4o) 的多模态能力强
- **长文档阅读（论文）**：Claude 的长上下文窗口是优势
- **日常随手问**：哪个方便用哪个，差异不大

### 费用参考（2026年初）

| 产品 | 免费版 | 付费版（月费） |
|------|--------|----------------|
| Claude | 有限免费（Sonnet） | Pro $20/月（Opus） |
| ChatGPT | 免费（GPT-4o mini） | Plus $20/月（GPT-4o） |
| DeepSeek | 免费 | 暂无付费版 |

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

### 选择建议

- **MATLAB 编程**：Copilot 不直接支持 MATLAB，用 Cursor + 对话式 AI 更实际
- **Python/LabVIEW脚本**：Copilot 或 Cursor 都可以
- **VBA/Excel**：Copilot 支持较好
- **日常多语言**：Cursor 的项目级理解能力更全面

### 费用参考

| 产品 | 个人版 | 学生版 |
|------|--------|--------|
| GitHub Copilot | $10/月 | 免费（GitHub Education） |
| Cursor | $20/月 | 暂无 |
| Windsurf | 有免费额度 | 暂无 |

> 强烈建议：先注册 GitHub Education（只需学校邮箱），免费获得 Copilot。

> 编程类工具的月费、学生政策同样可能变更，以 GitHub、Cursor、Windsurf 等官网为准。

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

---

## 五、与各科研软件的配合方式

不同软件和 AI 的配合方式不同，核心思路如下：

| 软件 | AI配合方式 | 主要AI工具 |
|------|-----------|-----------|
| Origin | 对话式AI生成脚本 + Python接口 | Claude/DeepSeek |
| MATLAB | 对话式AI生成.m代码 + Copilot辅助 | Claude + Cursor |
| Excel | 对话式AI生成公式/VBA + Copilot | ChatGPT + Copilot |
| COMSOL | 对话式AI辅助建模思路 + Java API | Claude |
| FDTD | 对话式AI辅助脚本编写 | Claude/DeepSeek |
| SolidWorks | 对话式AI辅助建模思路 + 宏 | Claude |
| C4D | 对话式AI辅助 + Python脚本 | Claude |
| LabVIEW | 对话式AI辅助设计思路 | Claude/DeepSeek |

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
