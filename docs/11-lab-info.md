# 课题组信息与本地约定

本节用于补充**本课题组**的落地信息：账号、数据与协作方式。以下内容多为**通用建议**，请根据导师要求和个人情况调整；如组内后续形成统一规定，可在此补充。

---

## 推荐阅读方式

| 角色 | 说明 | 建议优先阅读 |
|------|------|----------------|
| **以实验为主** | 主要采集数据、使用仪器 | [前言](00-introduction.md) → [提示词模板](10-prompt-templates.md) 中「数据分析」「实验记录」→ [Origin](02-origin.md) / [Excel](04-excel.md) |
| **以编程与数据处理为主** | 大量脚本、批量处理 | [前言](00-introduction.md) → [AI工具指南](01-ai-tools-guide.md) → [MATLAB](03-matlab.md) / [Excel](04-excel.md) → [提示词模板](10-prompt-templates.md) |
| **以仿真与可视化为主** | 多物理场、光学仿真、三维出图 | [前言](00-introduction.md) → [COMSOL](05-comsol.md) / [FDTD](06-fdtd.md) / [SolidWorks](07-solidworks.md) / [C4D](08-c4d.md) |
| **仪器与自动化** | 测控、DAQ、仪器联调 | [LabVIEW](09-labview.md) → [提示词模板](10-prompt-templates.md) 中「代码生成」「报错调试」 |

---

## 账号与权限

- **学校邮箱 / GitHub**：建议用学校邮箱（.edu.cn 后缀）注册 GitHub，可免费获取 [GitHub Education](https://education.github.com) 权益（含 Copilot 免费等）。是否统一注册请与导师确认。
- **组内代码托管**：目前使用 GitHub 组织 [2Dmaterial-lab](https://github.com/2Dmaterial-lab) 管理共享项目。如组内另设 GitLab 等平台，请以导师通知为准。
- **软件许可证**：MATLAB、COMSOL、Origin 等大多通过**学校校园授权**获取，具体请查看学校信息化中心/软件下载平台，或咨询高年级同学。如学校未提供授权，可先使用学生版/试用版。

---

## 数据与代码存放

- **实验数据存放**：暂无统一路径规定。建议在个人电脑或实验室公用电脑上建立规范目录，例如：
  ```
  项目名/
  ├── raw_data/        # 原始数据，只读不动
  ├── processed_data/  # 处理后的数据
  ├── scripts/         # 处理脚本
  └── figures/         # 输出图表
  ```
- **命名建议**：文件名含日期和简短描述，如 `2026-04-12_transmittance_sampleA.csv`，避免用"新建文件夹""最终版"等模糊命名。
- **敏感数据**：未发表数据**不要**上传到云端 AI 服务；备份建议使用移动硬盘或实验室 NAS（如有）。

---

## 协作与答疑

- **日常问题**：优先在组会提出，或直接请教同方向的师兄师姐。
- **软件问题**：先查阅本手册对应章节和提示词模板，尝试用 AI 辅助解决；仍无法解决再在组内交流。
- **手册纠错与建议**：见仓库根目录 [CONTRIBUTING.md](https://github.com/2Dmaterial-lab/AIUserManual/blob/main/CONTRIBUTING.md)，或直接联系手册维护者。

---

## 校内政策与合规

若本校/本院对生成式 AI 的使用、论文署名或数据出境有正式文件，可在此列出**标题与链接**，便于同学在开题、投稿前自查。

- 暂无收集到相关文件。如有请补充，或以导师与学院要求为准。
- **底线原则**：AI 辅助可以用于代码生成、数据处理、语言润色，但论文的核心创新和结论必须是自己完成和验证的。具体边界请与导师沟通。

---

## 在线阅读地址

手册的**正式阅读地址**以课题组部署的站点为准（例如 GitHub Pages）。在 GitHub 上直接浏览 Markdown 时，目录与排版可能与站点略有差异，**请以网页版为准**。

当前地址：[https://2dmaterial-lab.github.io/AIUserManual/](https://2dmaterial-lab.github.io/AIUserManual/)
