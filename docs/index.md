# AI辅助科研工具使用说明

> 面向课题组研究生的 AI 辅助环境配置与工具使用指南

!!! tip "在线阅读"

    **正式版以课题组网站为准**（排版、搜索、目录与站内链接在构建后的站点中完整可用）。若仅在 GitHub 仓库里浏览原始 Markdown，请以部署后的网页为准。

    仓库与站点为公开访问，如需保密请参考仓库根目录 [README](https://github.com/2dmaterial-lab/AIUserManual/blob/main/README.md#许可与可见性) 中的「许可与可见性」。

## 快速开始

本手册帮助课题组成员快速上手科研常用软件，并学会利用 AI 工具显著提升工作效率。

**2026 年 5 月 19 日更新**：按当前公开信息刷新 AI 工具部分，覆盖 GPT-5.5、Claude Opus 4.7、Gemini 3.1 Pro、DeepSeek V4、GLM-5.1 等主流模型线；新增「MCP 协议与 AI 智能体」小节；补充工具选择速查、推荐工作流、Agent、终端 AI 编程工具（Claude Code / Codex CLI）、科研工作流、文献核查、可复现数据分析和科研数据安全建议；新增科研任务工作流、数据管理与可复现科研、入组第一周训练。

**建议阅读顺序**：

1. [前言：AI辅助科研的理念](00-introduction.md) — 了解正确心态和使用边界
2. [AI工具选择与使用指南](01-ai-tools-guide.md) — 选对工具，事半功倍
3. [科研任务工作流](12-research-workflows.md) — 从任务出发组织文献、数据、仿真和投稿
4. 按需阅读你使用的工具章节
5. [课题组信息与本地约定](11-lab-info.md) — 账号、数据与协作方式（请维护者按需填写）

## 按角色快速入口

| 你主要做… | 建议先读 | 常用工具章 |
|-----------|----------|------------|
| **实验与数据处理** | [AI工具指南](01-ai-tools-guide.md#tool-choice) → [提示词模板](10-prompt-templates.md)（数据分析 / 实验记录） | [Origin](02-origin.md)、[Excel](04-excel.md) |
| **编程、脚本、批量任务** | [前言](00-introduction.md) → [AI工具指南](01-ai-tools-guide.md) → [提示词模板](10-prompt-templates.md) | [MATLAB](03-matlab.md)、[Excel](04-excel.md) |
| **仿真与三维设计/渲染** | [前言](00-introduction.md) → 对应仿真或建模章 | [COMSOL](05-comsol.md)、[FDTD](06-fdtd.md)、[SolidWorks](07-solidworks.md)、[C4D](08-c4d.md) |
| **仪器、测控、自动化** | [LabVIEW 章](09-labview.md) → [提示词模板](10-prompt-templates.md)（代码与调试类） | [LabVIEW](09-labview.md) |
| **新入组同学** | [入组第一周训练](14-new-student-bootcamp.md) → [数据管理与可复现科研](13-data-reproducibility.md) | 按任务选择 |

更细的说明见 [课题组信息与本地约定](11-lab-info.md) 中的「推荐阅读方式」表格。

## 科研工作流

| 任务 | 章节 |
|------|------|
| 文献调研、数据作图、仿真扫描、仪器采集、投稿前检查 | [科研任务工作流](12-research-workflows.md) |
| 原始数据保护、目录结构、README、图表追溯、AI 使用记录 | [数据管理与可复现科研](13-data-reproducibility.md) |
| 新生 5 天训练任务：工具边界、文献表、复现图、报错调试、小闭环 | [入组第一周训练](14-new-student-bootcamp.md) |

## 工具指南

| 工具 | 用途 | 章节 |
|------|------|------|
| Origin | 数据绘图与分析 | [查看指南](02-origin.md) |
| MATLAB | 数值计算与编程 | [查看指南](03-matlab.md) |
| Excel | 数据处理与可视化 | [查看指南](04-excel.md) |
| COMSOL | 多物理场仿真 | [查看指南](05-comsol.md) |
| FDTD | 光学仿真 | [查看指南](06-fdtd.md) |
| SolidWorks | 三维机械建模 | [查看指南](07-solidworks.md) |
| C4D | 三维可视化渲染 | [查看指南](08-c4d.md) |
| LabVIEW | 仪器控制编程 | [查看指南](09-labview.md) |

## 提示词模板

日常科研中可以直接复制使用的 AI 提示词模板，覆盖代码生成、报错调试、数据分析、文献证据表、论文写作、AI 使用记录等场景。

[查看提示词模板](10-prompt-templates.md)

## 修订记录

主要修订见 [更新日志](changelog.md)。
