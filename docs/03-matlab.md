# MATLAB — AI辅助使用指南

> **本章导读**：按「简介与场景 → 安装配置 → AI 辅助技巧 → 示例与排错 → 进阶资源」组织，可按需跳读。

!!! info "版本与功能时效"

    本章按 MATLAB/Simulink R2026a 公开资料和常见科研脚本工作流整理。不同学校授权的工具箱差异很大，使用 AI 生成代码前请确认 MATLAB 版本、已安装工具箱和目标运行环境。

## 1. 简介与适用场景

MATLAB 是矩阵实验室（Matrix Laboratory）的缩写，是科研领域最广泛使用的数值计算和编程环境。在课题组中，MATLAB 主要用于：

- **数据处理**：光谱数据、图像数据、信号数据的分析与处理
- **数值计算**：矩阵运算、微分方程求解、最优化
- **信号处理**：FFT、滤波、频谱分析
- **绘图与可视化**：publication 级别的科学绘图
- **仿真**：配合 Simulink 进行系统仿真
- **自动化**：批量处理实验数据、自动化测试流程

### 2026 年可关注的变化

- **R2026a**：MathWorks 已发布 R2026a，包含性能、图形/App 构建和 Simulink 工作流更新。
- **Simulink Copilot**：R2026a 引入面向工程系统开发的生成式 AI 能力；如果课题涉及控制、嵌入式或系统级仿真，可关注学校授权是否包含相关功能。
- **Python 互操作**：MATLAB 与 Python 联合工作越来越常见，适合把仪器数据处理、机器学习或批量文件处理拆到 Python，再用 MATLAB 做既有分析流程。
- **可复现实验记录**：论文脚本建议记录 `version`、工具箱版本、随机种子和输入数据哈希。

## 2. 安装与配置

### 获取方式

大多数高校都有 MATLAB 校园授权（Site License），通过学校网络即可免费使用：

1. 访问 [mathworks.com](https://www.mathworks.com)
2. 用学校邮箱注册 MathWorks 账号
3. 在学校网络环境下（或连接校园VPN）激活许可证
4. 下载并安装 MATLAB

### 安装要点

- **选择性安装工具箱**：默认安装所有工具箱会占用大量空间。建议先安装基础包，后续按需添加：
  - 信号处理：Signal Processing Toolbox
  - 图像处理：Image Processing Toolbox
  - 统计分析：Statistics and Machine Learning Toolbox
  - 曲线拟合：Curve Fitting Toolbox
  - 优化：Optimization Toolbox
- **路径设置**：将常用脚本文件夹添加到 MATLAB 路径：`Set Path → Add with Subfolders`
- **编辑器配置**：开启自动补全、代码折叠、实时编辑器

### 推荐的初始配置

```matlab
% 在 startup.m 中添加（位于 ~/Documents/MATLAB/startup.m）
% 设置默认绘图字体和线宽
set(0, 'DefaultAxesFontSize', 12);
set(0, 'DefaultAxesFontName', 'Helvetica');
set(0, 'DefaultLineLineWidth', 1.5);
set(0, 'DefaultFigureColor', 'w');
set(0, 'DefaultAxesColor', 'k');
```

## 3. AI辅助使用核心技巧

### 对话式AI（Claude/ChatGPT/DeepSeek）

#### 生成代码

最直接的用法——描述你的需求，让 AI 生成 MATLAB 代码：

- **明确输入输出**：告诉 AI 数据的维度、格式、想要的结果
- **指定工具箱**：如果需要特定工具箱函数，明确说明
- **要求注释**：让 AI 在代码中添加注释，方便理解和修改

#### 解读报错

将 MATLAB 的错误信息完整复制给 AI：

- 包含完整的错误堆栈（stack trace）
- 说明你想要实现什么
- AI 通常能快速定位问题并给出修复方案

#### 优化代码

已有可运行但效率低下的代码，让 AI 帮你优化：

- 向量化替代循环
- 预分配内存
- 使用更高效的内置函数

### 编程辅助AI（Claude Code/Codex/Cursor/Copilot）

- **Claude Code / Codex CLI**：适合维护包含多个 `.m`、测试数据和导出图脚本的项目。让 Agent 改代码前，限定目录并要求运行最小测试。
- **Cursor**：适合在项目内搜索函数依赖、重构批处理脚本、解释较长的 MATLAB 文件。
- **Copilot**：在 VS Code 中编辑 `.m` 文件时可提供补全。
- 注意：多数 AI 工具对 MATLAB 的理解不如 Python 稳定，关键数值结果必须自己验证。

### AI 生成代码的验收清单

1. **先跑小样本**：用 5–10 行数据或已知答案验证输入输出。
2. **检查工具箱依赖**：让 AI 列出用到的工具箱和替代实现。
3. **固定随机性**：涉及拟合、优化、机器学习时设置 `rng(seed)`。
4. **记录环境**：在脚本开头输出 `version`、`ver`、输入文件名和关键参数。
5. **图表可复现**：论文图不要只保存 `.fig`，同时保存生成脚本、原始数据和导出命令。

## 4. 常见任务与提示词示例

### 场景1：信号处理 — FFT频谱分析

**提示词**：

> 我有一组时域信号数据存储在 CSV 文件中，第一列是时间(秒)，第二列是幅值。采样率是 10kHz。请帮我写一个 MATLAB 脚本，完成以下任务：
> 1. 读取 CSV 数据
> 2. 去除直流分量
> 3. 做FFT变换，计算幅度谱
> 4. 画出频谱图，x轴为频率(Hz)，y轴为幅值，只显示0-2000Hz范围
> 5. 标注峰值频率
> 要求：使用汉宁窗，输出300dpi的PNG图片

**预期输出**：完整的 .m 脚本，包含数据读取、预处理、FFT、绘图

```matlab
% FFT频谱分析脚本
data = readmatrix('signal_data.csv');
t = data(:, 1);
signal = data(:, 2);

% 参数
fs = 10000;  % 采样率 10kHz
N = length(signal);

% 去除直流分量
signal = signal - mean(signal);

% 汉宁窗
window = hanning(N);
signal_windowed = signal .* window;

% FFT
Y = fft(signal_windowed);
P2 = abs(Y / N);          % 双边谱
P1 = P2(1:N/2+1);         % 单边谱
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(N/2))/N;

% 绘图
figure('Position', [100 100 800 500]);
plot(f, P1, 'LineWidth', 1.5);
xlim([0 2000]);
xlabel('Frequency (Hz)');
ylabel('Amplitude');
title('FFT Spectrum');

% 标注峰值
[~, idx] = max(P1);
text(f(idx), P1(idx), sprintf('  Peak: %.1f Hz', f(idx)), ...
    'FontSize', 11, 'Color', 'r');

print('fft_spectrum', '-dpng', '-r300');
```

### 场景2：Publication级别绘图

**提示词**：

> 请帮我写一个 MATLAB 绘图脚本，要求符合论文发表标准：
> - 有3组数据需要画在同一个图中（3条线），数据分别存在 data1.csv, data2.csv, data3.csv
> - 每个CSV第一列是x（波长nm），第二列是y（透过率%）
> - 使用不同颜色和线型区分（实线、虚线、点划线）
> - 图例放在图内右上角
> - 字体统一 Helvetica 12pt
> - 坐标轴加粗，线宽1.5pt
> - 输出为 EPS 格式，适合 LaTeX 论文使用
> - 图片尺寸 8cm x 6cm（双栏论文的半栏宽度）

**预期输出**：完整绘图脚本

```matlab
% Publication-quality plotting
figure('Units', 'centimeters', 'Position', [2 2 8 6]);

% 读取数据
d1 = readmatrix('data1.csv');
d2 = readmatrix('data2.csv');
d3 = readmatrix('data3.csv');

% 绘图
h1 = plot(d1(:,1), d1(:,2), 'k-', 'LineWidth', 1.5); hold on;
h2 = plot(d2(:,1), d2(:,2), 'r--', 'LineWidth', 1.5);
h3 = plot(d3(:,1), d3(:,2), 'b-.', 'LineWidth', 1.5);

% 格式设置
set(gca, 'FontSize', 12, 'FontName', 'Helvetica', ...
    'LineWidth', 1.2, 'Box', 'on');
xlabel('Wavelength (nm)');
ylabel('Transmittance (%)');

% 图例
legend([h1 h2 h3], {'Sample A', 'Sample B', 'Sample C'}, ...
    'Location', 'northeast', 'FontSize', 10);

% 输出
print('transmittance', '-depsc', '-r300');
```

### 场景3：自定义模型曲线拟合

**提示词**：

> 我需要用 MATLAB 对实验数据进行非线性曲线拟合。我的物理模型是一个洛伦兹峰：
> y = A * (gamma/2)^2 / ((x - x0)^2 + (gamma/2)^2) + B
> 其中 A 是振幅，x0 是中心频率，gamma 是半高全宽(FWHM)，B 是基线偏移。
>
> 实验数据在 fit_data.csv 中，第一列是 x，第二列是 y。
> 请帮我：
> 1. 写拟合代码，用 lsqcurvefit 或 fit 函数
> 2. 设置合理的初始猜测值（x0大约在1550附近）
> 3. 画出原始数据和拟合曲线的对比图
> 4. 输出拟合参数和95%置信区间
> 5. 计算R-squared

**预期输出**：完整拟合脚本

```matlab
% Lorentzian curve fitting
data = readmatrix('fit_data.csv');
xdata = data(:, 1);
ydata = data(:, 2);

% Lorentzian 模型
lorentz = @(p, x) p(1) * (p(3)/2)^2 ./ ((x - p(2)).^2 + (p(3)/2)^2) + p(4);

% 初始猜测 [A, x0, gamma, B]
p0 = [1, 1550, 10, 0];

% 拟合
[p_fit, resnorm, residual, exitflag, output, lambda, jacobian] = ...
    lsqcurvefit(lorentz, p0, xdata, ydata);

% 置信区间
ci = nlparci(p_fit, residual, jacobian);

% R-squared
SS_res = sum(residual.^2);
SS_tot = sum((ydata - mean(ydata)).^2);
R2 = 1 - SS_res / SS_tot;

% 输出结果
fprintf('A     = %.4f  [%.4f, %.4f]\n', p_fit(1), ci(1,1), ci(1,2));
fprintf('x0    = %.4f  [%.4f, %.4f]\n', p_fit(2), ci(2,1), ci(2,2));
fprintf('gamma = %.4f  [%.4f, %.4f]\n', p_fit(3), ci(3,1), ci(3,2));
fprintf('B     = %.4f  [%.4f, %.4f]\n', p_fit(4), ci(4,1), ci(4,2));
fprintf('R^2   = %.6f\n', R2);

% 绘图
figure;
plot(xdata, ydata, 'ko', 'MarkerSize', 4, 'MarkerFaceColor', 'k'); hold on;
xfine = linspace(min(xdata), max(xdata), 500);
plot(xfine, lorentz(p_fit, xfine), 'r-', 'LineWidth', 1.5);
xlabel('Frequency (THz)'); ylabel('Intensity (a.u.)');
legend('Data', 'Lorentzian Fit', 'Location', 'northwest');
```

### 场景4：批量数据处理

**提示词**：

> 我有一个文件夹 data/，里面有100个 CSV 文件，命名格式为 sample_001.csv 到 sample_100.csv。每个文件结构相同：第一列波长(nm)，第二列透过率(%)。
>
> 请帮我写一个脚本：
> 1. 自动遍历所有CSV文件
> 2. 对每个文件计算：中心波长、峰值透过率、半高全宽(FWHM)
> 3. 将所有结果汇总到一个表格并保存为 results.csv
> 4. 画出100条曲线的叠加图

**预期输出**：批量处理脚本

```matlab
% Batch data processing
fileList = dir('data/sample_*.csv');
nFiles = length(fileList);
results = zeros(nFiles, 4);  % [filename, center, peak, FWHM]

figure; hold on;
colors = parula(nFiles);

for i = 1:nFiles
    % 读取数据
    data = readmatrix(fullfile('data', fileList(i).name));
    wavelength = data(:, 1);
    transmittance = data(:, 2);

    % 绘制叠加图
    plot(wavelength, transmittance, 'Color', colors(i,:));

    % 计算指标
    [peak_val, peak_idx] = max(transmittance);
    center_wl = wavelength(peak_idx);

    % FWHM 计算
    half_max = peak_val / 2;
    above_half = transmittance >= half_max;
    fwhm = wavelength(find(above_half, 1, 'last')) - ...
           wavelength(find(above_half, 1, 'first'));

    results(i, :) = [i, center_wl, peak_val, fwhm];
end

xlabel('Wavelength (nm)'); ylabel('Transmittance (%)');
title('All Samples Overlay');

% 保存结果
T = array2table(results, 'VariableNames', ...
    {'SampleID', 'CenterWavelength', 'PeakTransmittance', 'FWHM'});
writetable(T, 'results.csv');
```

### 场景5：调试报错

**提示词**：

> 我运行以下 MATLAB 代码时报错了，请帮我分析和修复：
>
> ```matlab
> A = rand(100, 3);
> B = rand(50, 3);
> C = A * B';
> ```
>
> 错误信息：
> ```
> Error using  *
> Incorrect dimensions for matrix multiplication.
> ```
>
> 我想计算 A 中每行和 B 中每行的欧氏距离，得到 100x50 的距离矩阵。

**预期输出**：AI 会解释维度不匹配的原因，并给出正确的实现方式

```matlab
% 方法1：循环（直观但较慢）
C = zeros(100, 50);
for i = 1:100
    for j = 1:50
        C(i,j) = norm(A(i,:) - B(j,:));
    end
end

% 方法2：向量化（推荐，更快）
C = pdist2(A, B);  % 需要 Statistics Toolbox

% 方法3：纯向量化（无需工具箱）
C = sqrt(sum(A.^2, 2) + sum(B.^2, 2)' - 2 * A * B');
```

## 5. 常见问题与排错

### AI能帮你快速解决的问题

| 问题 | AI协助方式 |
|------|-----------|
| 函数用法不清楚 | 直接问 AI，比查文档快 |
| 矩阵维度不匹配 | 贴出错误信息和代码，AI 通常秒解 |
| 绘图格式调整 | 描述你想要的效果，AI 生成格式代码 |
| 工具箱函数选择 | 描述任务，AI 推荐最合适的函数 |
| 代码运行太慢 | 贴出代码，AI 帮你向量化优化 |

### 需要人工判断的注意事项

- **数值精度**：AI 生成的算法可能不够数值稳定，需自行验证
- **物理合理性**：拟合结果的物理意义必须人工判断
- **工具箱依赖**：AI 可能使用了你没有安装的工具箱函数，注意检查
- **版本差异**：AI 可能用较新版本的语法，旧版 MATLAB 可能不支持

### 常见报错速查

| 报错 | 常见原因 | 快速修复 |
|------|---------|---------|
| `Index exceeds matrix dimensions` | 索引越界 | 检查矩阵大小，用 `size()` 确认 |
| `Incorrect dimensions for matrix multiplication` | 维度不匹配 | 检查 `size(A)` 和 `size(B)` |
| `Undefined function or variable` | 变量未定义或函数不存在 | 检查拼写、路径、工具箱 |
| `Not enough input arguments` | 函数调用参数不够 | 查看函数签名 `help funcName` |

## 6. 进阶资源

### 本仓库示例脚本

以下文件位于 `docs/assets/examples/`，构建站点后也可通过站点内链接直接下载；克隆本仓库时路径相同。

- [matlab_publication_plot.m](assets/examples/matlab_publication_plot.m) — publication 级别折线图模板（含尺寸、字体、导出格式）
- [matlab_fft_spectrum.m](assets/examples/matlab_fft_spectrum.m) — FFT 与频谱分析示例

### 官方文档

- MATLAB 官方文档：[mathworks.com/help/matlab](https://www.mathworks.com/help/matlab/)
- MATLAB Academy（免费在线课程）：[mathworks.com/learn/tutorials/matlab-onramp](https://www.mathworks.com/learn/tutorials/matlab-onramp)
- MATLAB/Simulink 最新功能：[mathworks.com/products/new_products/latest_features.html](https://www.mathworks.com/products/new_products/latest_features.html)

### 推荐学习路径

1. **入门**：MATLAB Onramp（官方免费，2小时）
2. **进阶**：掌握向量化编程、cell/struct 数据类型、函数句柄
3. **高级**：面向对象编程、MEX文件（C/C++混合编程）、App Designer

### 实用技巧

- 用 `doc funcName` 替代 `help funcName`，打开更详细的帮助文档
- 用 `Ctrl+I` 自动缩进代码
- 用 `tic; ... toc;` 计时
- 用 `profile on; ... profile viewer;` 性能分析
