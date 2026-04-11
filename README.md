# AI辅助科研工具使用说明

> 面向课题组研究生的 AI 辅助环境配置与工具使用指南

**在线阅读（正式版）**：<https://2dmaterial-lab.github.io/AIUserManual/>

若仅在 GitHub 上浏览本仓库中的 Markdown，目录与渲染可能与站点不一致，**请以部署后的网页为准**。主要修订见 [docs/changelog.md](docs/changelog.md)。

## 项目简介

本手册旨在帮助课题组成员快速上手科研常用软件，并学会利用 AI 工具（Claude、ChatGPT、DeepSeek、Copilot、Cursor 等）显著提升工作效率。

**核心理念**：AI 不是替代你思考，而是帮你把重复性工作自动化，把精力留给真正需要创造力的事情。

## 目录导航

### 基础篇

| 章节 | 内容 | 链接 |
|------|------|------|
| 00 | 前言：AI辅助科研的理念与心态 | [introduction.md](docs/00-introduction.md) |
| 01 | AI工具选择与使用指南 | [ai-tools-guide.md](docs/01-ai-tools-guide.md) |

### 工具篇

| 章节 | 工具 | 用途 | 链接 |
|------|------|------|------|
| 02 | Origin | 数据绘图与分析 | [origin.md](docs/02-origin.md) |
| 03 | MATLAB | 数值计算与编程 | [matlab.md](docs/03-matlab.md) |
| 04 | Excel | 数据处理与可视化 | [excel.md](docs/04-excel.md) |
| 05 | COMSOL | 多物理场仿真 | [comsol.md](docs/05-comsol.md) |
| 06 | FDTD | 光学仿真 | [fdtd.md](docs/06-fdtd.md) |
| 07 | SolidWorks | 三维机械建模 | [solidworks.md](docs/07-solidworks.md) |
| 08 | C4D | 三维可视化渲染 | [c4d.md](docs/08-c4d.md) |
| 09 | LabVIEW | 仪器控制编程 | [labview.md](docs/09-labview.md) |

### 模板篇

| 章节 | 内容 | 链接 |
|------|------|------|
| 10 | 通用提示词模板集合 | [prompt-templates.md](docs/10-prompt-templates.md) |

## 使用建议

- **新生**：建议从 00、01 开始，了解 AI 辅助的理念和工具选择，再按需阅读具体工具章节
- **有基础的同学**：直接跳到你使用的工具章节，重点看"AI辅助使用核心技巧"和"提示词示例"部分
- **所有人**：收藏第 10 章的提示词模板，日常科研中可以直接复制使用

## 本地构建站点（MkDocs）

如需离线阅读或部署为网页：

```bash
cd AIUserManual
pip install -r requirements.txt
mkdocs serve    # 浏览器访问提示的本地地址预览
# mkdocs build  # 生成 site/ 静态文件
```

说明与依赖版本见项目根目录 `requirements.txt`。

## 示例脚本

各章「进阶资源」中已挂链；文件统一放在 `docs/assets/examples/`，与 MkDocs 构建产物一并发布。

| 文件 | 说明 |
|------|------|
| [matlab_publication_plot.m](docs/assets/examples/matlab_publication_plot.m) | MATLAB 论文级出图模板 |
| [matlab_fft_spectrum.m](docs/assets/examples/matlab_fft_spectrum.m) | MATLAB FFT / 频谱示例 |
| [excel_batch_process.bas](docs/assets/examples/excel_batch_process.bas) | Excel VBA 批量处理示例 |
| [fdtd_waveguide.lsf](docs/assets/examples/fdtd_waveguide.lsf) | Lumerical FDTD 脚本示例 |
| [c4d_batch_render.py](docs/assets/examples/c4d_batch_render.py) | C4D Python 批量渲染示例 |

## 贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。摘要如下：

1. 发现错误或过时信息，请提出修改
2. 有好的 AI 使用技巧或提示词，欢迎补充
3. 新增工具章节请遵循现有模板格式（简介 → 安装配置 → AI 辅助技巧 → 提示词示例 → 排错 → 进阶资源）
4. 新增可下载脚本时，请放入 `docs/assets/examples/`，文件名使用小写加下划线，并在对应章节的「进阶资源」中加链接说明用途

## 许可

本手册仅供课题组内部使用，请勿外传。
