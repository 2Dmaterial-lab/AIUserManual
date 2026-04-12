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

### 附录

| 章节 | 内容 | 链接 |
|------|------|------|
| 11 | 课题组信息与本地约定 | [11-lab-info.md](docs/11-lab-info.md) |
| — | 更新日志（主要修订） | [changelog.md](docs/changelog.md) |

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

## 访问统计（可选）

在线站点可接入 **Google Analytics 4（GA4）**，在 [Google 分析](https://analytics.google.com/) 后台查看访问量、页面浏览与流量来源等（静态站本身不保存访问日志）。

1. 在 GA4 中为该网站创建**数据流**，复制**衡量 ID**（格式 `G-xxxxxxxxxx`）。
2. 打开本仓库 **Settings → Secrets and variables → Actions**，新建仓库密钥 **`GOOGLE_ANALYTICS_ID`**，值为上述衡量 ID。推送 `main` 后的部署构建会自动注入该变量。
3. 本地验证：可先执行 `export GOOGLE_ANALYTICS_ID=G-你的ID`，再 `mkdocs serve` 或 `mkdocs build`，在生成的页面中应能看到对 `googletagmanager.com` 的请求（浏览器开发者工具 → 网络）。

未配置该密钥时，站点**不会**加载任何统计脚本。若部分访问者网络无法连接 Google 服务，统计可能不完整，属正常现象。

### 页脚「全站累计约 ×× 次页面浏览」（可选）

在页脚展示**约计总浏览量**（数据来自 GA4 的 `screenPageViews` 汇总，非实时秒级）。需要在 **Google Cloud** 侧启用 **Google Analytics Data API**，并为本仓库配置两个 **Actions Secret**（与上方的 `GOOGLE_ANALYTICS_ID` 是不同用途，需同时配置才会在页脚看到数字）：

| Secret 名称 | 内容 |
|-------------|------|
| `GA_SERVICE_ACCOUNT_JSON` | Google Cloud **服务账号** 的 JSON 密钥全文（多行粘贴到 Secret 中）。 |
| `GA4_PROPERTY_ID` | GA4 **媒体资源 ID**（纯数字，如 `123456789`；在 GA「管理 → 媒体资源设置」中查看，**不是** `G-` 开头的衡量 ID）。 |

**Google Cloud 简要步骤**（需有权限操作 GCP 与 GA4 媒体资源）：

1. 打开 [Google Cloud Console](https://console.cloud.google.com/)，选择或新建项目。  
2. 「API 和服务 → 已启用的 API」→ 启用 **Google Analytics Data API**。  
3. 「IAM 和管理 → 服务账号」→ 创建服务账号 →「密钥」→ 添加 **JSON** 密钥并下载；将 JSON **整份**粘贴到仓库 Secret `GA_SERVICE_ACCOUNT_JSON`。  
4. 打开 [Google Analytics](https://analytics.google.com/) → **管理**（齿轮）→ 选中你的 **媒体资源** → **媒体资源访问管理** → **新增使用者**，填入服务账号邮箱（形如 `xxx@项目id.iam.gserviceaccount.com`），角色选 **查看者**。  
5. 仍在「管理」→ **媒体资源设置** 中复制 **媒体资源 ID**（数字），写入 Secret `GA4_PROPERTY_ID`。

配置完成后，推送 `main` 触发部署：构建前会运行 `scripts/fetch_ga_stats.py` 拉取累计值并写入 `docs/assets/analytics-stats.json`，页脚脚本会读取并显示。**请勿**将服务账号 JSON 提交到 Git，仅放在 GitHub Secrets。

本地可安装 `pip install -r scripts/requirements-analytics.txt` 后导出上述两个环境变量，运行 `python scripts/fetch_ga_stats.py` 再 `mkdocs serve` 预览页脚效果。

## 示例脚本

各章「进阶资源」中已挂链；文件统一放在 `docs/assets/examples/`，与 MkDocs 构建产物一并发布。

| 文件 | 说明 |
|------|------|
| [matlab_publication_plot.m](docs/assets/examples/matlab_publication_plot.m) | MATLAB 论文级出图模板 |
| [matlab_fft_spectrum.m](docs/assets/examples/matlab_fft_spectrum.m) | MATLAB FFT / 频谱示例 |
| [excel_batch_process.bas](docs/assets/examples/excel_batch_process.bas) | Excel VBA 批量处理示例 |
| [fdtd_waveguide.lsf](docs/assets/examples/fdtd_waveguide.lsf) | Lumerical FDTD 脚本示例 |
| [c4d_batch_render.py](docs/assets/examples/c4d_batch_render.py) | C4D Python 批量渲染示例 |

### 测试数据

示例脚本引用的数据文件放在 `docs/assets/test_data/`，可直接用于验证脚本运行效果。

| 文件 | 说明 |
|------|------|
| [data1.csv](docs/assets/test_data/data1.csv) | MATLAB 绘图示例 — Sample A 透射率数据 |
| [data2.csv](docs/assets/test_data/data2.csv) | MATLAB 绘图示例 — Sample B 透射率数据 |
| [data3.csv](docs/assets/test_data/data3.csv) | MATLAB 绘图示例 — Sample C 透射率数据 |
| [signal_data.csv](docs/assets/test_data/signal_data.csv) | MATLAB FFT 示例 — 采样信号数据 |

## 贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。摘要如下：

1. 发现错误或过时信息，请提出修改
2. 有好的 AI 使用技巧或提示词，欢迎补充
3. 新增工具章节请遵循现有模板格式（简介 → 安装配置 → AI 辅助技巧 → 提示词示例 → 排错 → 进阶资源）
4. 新增可下载脚本时，请放入 `docs/assets/examples/`，文件名使用小写加下划线，并在对应章节的「进阶资源」中加链接说明用途

## 许可与可见性

本手册仅供课题组内部学习与交流使用，请勿擅自对外传播。仓库与 GitHub Pages 站点为公开访问，搜索引擎可收录。若课题或学校对数据与资料有更高保密要求，请将仓库设为 private 或结合校内部署等方式另行约定。

若需将手册完全限制在校内或组内网络，请与导师或信息化部门确认可行方案。
