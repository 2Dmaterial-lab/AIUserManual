# FDTD — AI辅助使用指南

> **本章导读**：按「简介与场景 → 安装配置 → AI 辅助技巧 → 示例与排错 → 进阶资源」组织，可按需跳读。

!!! info "版本与功能时效"

    本章按 Ansys Lumerical / Ansys 2026 R1 附近的公开资料和常见光子器件仿真流程整理。Lumerical 产品名、许可证、GPU/HPC 支持和脚本 API 会随 Ansys 版本更新；请以本机 Help 与学校授权为准。

## 1. 简介与适用场景

FDTD（时域有限差分法）是求解麦克斯韦方程组的数值方法，在光学仿真中广泛应用。本指南以 Ansys Lumerical FDTD Solutions 为主，它是课题组最常用的 FDTD 商业软件。

主要应用场景：

- **光子器件仿真**：波导、光栅、耦合器、谐振腔
- **超表面/超材料**：单元结构设计和相位响应
- **散射问题**：纳米粒子散射、Mie 散射
- **近场光学**：等离激元、近场增强
- **与MATLAB联合**：FDTD 仿真 + MATLAB 优化

### 什么时候优先用 FDTD

| 场景 | 建议 | 原因 |
|------|------|------|
| 波导、光栅、耦合器、谐振腔等光子器件 | 推荐 | 适合全波电磁传播问题 |
| 需要近场、远场、S 参数或透射谱 | 推荐 | 监视器和脚本体系成熟 |
| 大量结构参数扫描 | 推荐脚本化使用 | Lumerical Script / Python API 可复现 |
| 只需要简化模式求解 | 谨慎 | MODE 或解析模型可能更快 |
| 不清楚边界和网格就直接扫参数 | 不推荐 | 容易得到看似平滑但错误的结果 |

### AI 能做 / 不能做

| AI 适合做 | 必须人工确认 |
|-----------|--------------|
| 生成 Lumerical Script / Python API 框架 | 材料库名称、色散模型和损耗 |
| 建议光源、监视器和扫描参数 | PML、对称性、源偏振和监视器位置 |
| 排查脚本报错和导出数据格式 | 网格收敛、仿真时间和能量守恒 |
| 把结果导出到 MATLAB/Python 后处理 | 物理解释和论文结论 |

### 最小闭环案例

1. 运行 `docs/assets/examples/fdtd_waveguide.lsf` 的简化波导模板。
2. 修改一个参数，如波导宽度，做 2-3 个测试点。
3. 导出传输谱为 CSV/MAT。
4. 检查材料、边界、mesh override、monitor 位置和 auto shutoff。

### 2026 年可关注的变化

- **Ansys 2026 R1**：Ansys 2026 R1 强调多产品工程工作流和 AI-powered 产品更新，光子设计中更常见 FDTD、MODE、INTERCONNECT 与版图/电路工具联动。
- **Lumerical 与系统级光子设计**：如果课题涉及光子集成电路，不要只停留在单个 FDTD 仿真；可把器件级 S 参数导出到 INTERCONNECT 或其他系统级工具。
- **材料库与色散模型**：新版材料库和旧脚本可能存在名称差异，AI 生成脚本后要核对材料名、拟合波段和损耗模型。
- **HPC/GPU 设置**：是否启用 GPU 或并行计算取决于许可证和硬件，性能提升不能假定，需用小模型实测。

## 2. 安装与配置

### 获取方式

- **Ansys 学术授权**：学校通过 Ansys 学术计划获取，联系学校 IT 部门
- **Lumerical 试用版**：30天全功能试用
- **下载地址**：[ansys.com/products/photonics](https://www.ansys.com/products/photonics)

### 安装要点

- Lumerical 现在是 Ansys 产品线的一部分，安装时选择 Ansys Photonics
- 需要安装 Ansys License Manager
- 推荐安装的配套工具：
  - MODE Solutions：波导模式求解器
  - INTERCONNECT：光子集成电路仿真
  - Lumerical Script：内置脚本环境

### 推荐配置

1. **硬件要求**：FDTD 计算量大，建议 32GB+ RAM、多核 CPU
2. **GPU 加速**：Lumerical 支持 GPU 加速，如果有 NVIDIA GPU 建议启用
3. **临时文件目录**：设置到大容量磁盘，FDTD 仿真会产生大量临时文件

## 3. AI辅助使用核心技巧

### 对话式AI（Claude/ChatGPT/DeepSeek）

Lumerical 有自己的脚本语言（类似 MATLAB 语法），AI 对其支持还不错：

#### 脚本生成

- 描述你的器件结构和仿真需求，AI 生成 Lumerical 脚本
- AI 可以生成参数扫描、优化循环的脚本
- 适合批量创建几何结构、设置仿真参数

#### 建模策略

- AI 可以建议仿真区域大小、PML 设置、网格精度
- 帮助选择合适的监视器类型（频域/时域/功率）
- 指导如何正确提取 S 参数

#### 调试报错

- Lumerical 脚本报错信息相对清晰，AI 通常能直接修复
- 仿真发散问题，AI 可以提供排查思路

### AI 辅助 FDTD 的验收清单

1. **材料不要只用常数折射率**：论文级结果应使用材料库或自定义色散数据，并说明来源。
2. **网格与时间收敛**：检查 mesh accuracy、局部 mesh override、auto shutoff min 和仿真时间。
3. **边界条件核对**：PML 厚度、对称/反对称边界方向和源偏振必须人工检查。
4. **监视器位置**：功率监视器和模式展开监视器要避开近场扰动区。
5. **脚本可复现**：保存 `.lsf`、材料文件、参数表和导出数据，不只保存 `.fsp`。

## 4. 常见任务与提示词示例

### 场景1：波导耦合器仿真

**提示词**：

> 我需要在 Lumerical FDTD 中仿真一个硅基条形波导，结构参数：
> - 波导宽度：500nm
> - 波导高度：220nm
> - 包层：SiO2（n=1.44），厚度 2um
> - 上包层：空气
> - 工作波长：1550nm
> - 波导长度：10um
>
> 请帮我写一个 Lumerical 脚本，完成：
> 1. 创建几何结构
> 2. 设置仿真区域和边界条件
> 3. 添加光源和监视器
> 4. 运行仿真并提取传输谱

**预期输出**：Lumerical 脚本

```lumerical
# 硅基波导 FDTD 仿真脚本

# 删除所有已有对象
deleteall;

# ===== 材料定义 =====
# Si 折射率（简化，实际应用中建议用材料库中的色散模型）
addrect;
set("name", "Si_core");
set("x", 0);
set("x span", 10e-6);
set("y", 0);
set("y span", 500e-9);    # 宽度 500nm
set("z", 110e-9);
set("z span", 220e-9);    # 高度 220nm
set("material", "Si (Silicon) - Palik");

# SiO2 下包层
addrect;
set("name", "SiO2_clad");
set("x", 0);
set("x span", 14e-6);
set("y", 0);
set("y span", 4e-6);
set("z", -890e-9);       # 底面在 -1um
set("z span", 2e-6);     # 厚度 2um
set("material", "SiO2 (Glass) - Palik");
set("alpha", 0.3);       # 半透明显示

# ===== 仿真区域 =====
addfdtd;
set("x", 0);
set("x span", 12e-6);
set("y", 0);
set("y span", 4e-6);
set("z", 0);
set("z span", 4e-6);
set("mesh accuracy", 3);    # 网格精度
set("pml type", "standard");

# ===== 光源 =====
addmode;
set("name", "source");
set("x", -4e-6);           # 光源位置
set("y", 0);
set("z", 0);
set("wavelength start", 1.5e-6);
set("wavelength stop", 1.6e-6);
set("direction", "Forward");

# ===== 监视器 =====
# 频域功率监视器 - 输出端
addpower;
set("name", "transmission");
set("monitor type", "2D X-normal");
set("x", 4e-6);
set("y", 0);
set("y span", 4e-6);
set("z", 0);
set("z span", 4e-6);

# 运行仿真
run;

# 提取传输谱
T = getresult("transmission", "T");
plot(T.lambda*1e6, T.T, "Wavelength (um)", "Transmission");
```

### 场景2：参数扫描

**提示词**：

> 我已经建好了一个光栅耦合器的 FDTD 模型，想用脚本做参数扫描。需要扫描：
> - 光栅周期 period：600nm 到 700nm，步长 5nm
> - 刻蚀深度 etch_depth：80nm 到 160nm，步长 10nm
>
> 每次仿真记录 1550nm 处的耦合效率。请写一个 Lumerical 参数扫描脚本。

**预期输出**：参数扫描脚本

```lumerical
# 光栅耦合器参数扫描脚本

# 定义参数范围
period_min = 600e-9;
period_max = 700e-9;
period_step = 5e-9;
n_period = (period_max - period_min) / period_step + 1;

etch_min = 80e-9;
etch_max = 160e-9;
etch_step = 10e-9;
n_etch = (etch_max - etch_min) / etch_step + 1;

# 结果存储
efficiency = matrix(n_period, n_etch);
periods = linspace(period_min, period_max, n_period);
etch_depths = linspace(etch_min, etch_max, n_etch);

# 扫描循环
for (i = 1:n_period) {
    for (j = 1:n_etch) {
        # 设置参数
        switchtolayout;
        setnamed("grating_period", "period", periods(i));
        setnamed("etch_region", "z span", etch_depths(j));

        # 运行仿真
        run;

        # 提取 1550nm 处传输效率
        T = getresult("transmission_monitor", "T");
        lambda = T.lambda;
        T_val = T.T;
        idx = find(lambda, 1550e-9);  # 找到1550nm
        efficiency(i, j) = T_val(idx);

        ?sprintf("Period=%.0fnm, Etch=%.0fnm, Eff=%.4f",
            periods(i)*1e9, etch_depths(j)*1e9, efficiency(i,j));
    }
}

# 绘制二维效率图
image(periods*1e9, etch_depths*1e9, efficiency,
    "Period (nm)", "Etch depth (nm)", "Coupling efficiency");

# 找到最优参数
max_eff = max(efficiency);
[i_max, j_max] = find(efficiency, max_eff);
?sprintf("最优: Period=%.0fnm, Etch=%.0fnm, Eff=%.4f",
    periods(i_max)*1e9, etch_depths(j_max)*1e9, max_eff);
```

### 场景3：S参数提取

**提示词**：

> 我在 Lumerical FDTD 中仿真了一个对称的 2x2 定向耦合器，需要提取完整的 S 参数矩阵（S11, S21, S31, S41）。
>
> 请告诉我：
> 1. 如何正确放置监视器
> 2. 如何用脚本提取 S 参数
> 3. 如何归一化 S 参数
> 4. 如何将结果导出给 MATLAB

**预期输出**：S 参数提取脚本

```lumerical
# S 参数提取脚本（2x2 定向耦合器）

# 确保有4个功率监视器（每个端口一个）
# Port1: input, Port2: through, Port3: cross1, Port4: cross2

# 提取各端口传输
T1 = getresult("port1_monitor", "T");  # 反射
T2 = getresult("port2_monitor", "T");  # 直通
T3 = getresult("port3_monitor", "T");  # 交叉
T4 = getresult("port4_monitor", "T");  # 交叉

lambda = T1.lambda;
S11 = sqrt(abs(T1.T));   # 反射系数
S21 = sqrt(abs(T2.T));   # 直通系数
S31 = sqrt(abs(T3.T));   # 交叉系数
S41 = sqrt(abs(T4.T));   # 交叉系数

# 绘制 S 参数
plot(lambda*1e6, abs(S21)^2, abs(S31)^2, abs(S11)^2,
    "Wavelength (um)", "Power",
    "S parameters");
legend("Through (S21)", "Cross (S31)", "Reflection (S11)");

# 导出到 MATLAB 格式
matlabsave("coupler_S_params.mat", lambda, S11, S21, S31, S41);
```

### 场景4：与MATLAB联合优化

**提示词**：

> 我想用 MATLAB 驱动 Lumerical FDTD 进行器件优化。具体流程：
> 1. MATLAB 定义优化算法（比如粒子群优化）
> 2. 每次迭代生成新的参数
> 3. 调用 Lumerical 运行仿真
> 4. 从结果文件中读取性能指标
> 5. 更新优化参数
>
> 请给出 MATLAB 端的代码框架。

**预期输出**：MATLAB + Lumerical 联合优化框架

```matlab
% MATLAB 驱动 Lumerical FDTD 优化
% 前提：Lumerical 已安装，且 MATLAB 可以调用 Lumerical API

% 初始化 Lumerical
hLum = lumopen();  % 打开 Lumerical

% 加载基础模型
lumeval(hLum, 'load(''grating_coupler.fsp'');');

% 优化参数定义
% x = [period, etch_depth, duty_cycle]
lb = [600, 80, 0.3];    % 下界 (nm)
ub = [700, 160, 0.7];   % 上界 (nm)

% 目标函数
objFun = @(x) runFDTD(hLum, x);

% 粒子群优化
options = optimoptions('particleswarm', ...
    'SwarmSize', 20, ...
    'MaxIterations', 50);
[x_opt, fval] = particleswarm(objFun, 3, lb, ub, options);

fprintf('最优参数: Period=%.1fnm, Etch=%.1fnm, Duty=%.2f\n', ...
    x_opt(1), x_opt(2), x_opt(3));
fprintf('最优耦合效率: %.4f\n', -fval);

lumclose(hLum);

%% 子函数：运行 FDTD 仿真
function eff = runFDTD(hLum, params)
    period = params(1);
    etch_depth = params(2);
    duty_cycle = params(3);

    % 设置参数
    lumeval(hLum, sprintf('setnamed("grating","period",%e);', period*1e-9));
    lumeval(hLum, sprintf('setnamed("etch","z span",%e);', etch_depth*1e-9));
    lumeval(hLum, sprintf('setnamed("grating","duty_cycle",%e);', duty_cycle));

    % 运行仿真
    lumeval(hLum, 'run;');

    % 提取结果
    T = lumeval(hLum, 'getresult("monitor","T");');
    lambda = T.lambda;
    T_val = T.T;

    % 找 1550nm 处的耦合效率（取负值因为要最小化）
    [~, idx] = min(abs(lambda - 1550e-9));
    eff = -T_val(idx);  % 取负值用于最小化
end
```

## 5. 常见问题与排错

### AI能帮你快速解决的问题

| 问题 | AI协助方式 |
|------|-----------|
| Lumerical 脚本语法 | 描述功能需求，AI 生成脚本 |
| 仿真发散 | 描述设置和现象，AI 排查原因 |
| S参数提取 | 描述器件类型，AI 给出监视器方案 |
| 网格设置 | 描述结构和波长，AI 建议网格参数 |
| 材料设置 | 描述材料，AI 推荐材料库选项 |

### 需要注意的事项

- **仿真时间**：FDTD 仿真可能很耗时，先用粗网格验证，再细网格精算
- **网格收敛性**：改变 mesh accuracy 检查结果是否收敛
- **PML 反射**：PML 距离结构至少半波长，注意 PML 类型选择
- **色散材料**：Lumerical 材料库中的色散模型需要确认适用波长范围
- **脚本兼容性**：不同版本 Lumerical 的脚本 API 可能有差异

### 常见问题速查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 仿真发散 | PML问题/光源设置/材料拟合 | 检查PML、降低网格精度排查、检查材料 |
| 结果不对称 | 网格偏移/结构不对称 | 检查网格对齐、确认结构对称性 |
| 传输率>1 | 归一化问题/监视器位置 | 检查光源归一化、监视器不要在PML内 |
| 运行极慢 | 网格过密/仿真域过大 | 先粗网格验证、缩小仿真域 |
| 与文献差异大 | 材料参数不同/网格不够 | 核对材料、做网格收敛测试 |

## 6. 进阶资源

### 本仓库示例脚本

以下文件位于 `docs/assets/examples/`，为 Lumerical 脚本示例，导入软件后请根据网格与材料自行核对。

- [fdtd_waveguide.lsf](assets/examples/fdtd_waveguide.lsf) — 波导类结构脚本示例

### 官方资源

- Lumerical 官方文档：[ansys.com/products/photonics](https://www.ansys.com/products/photonics)
- Lumerical KB（知识库）：[support.lumerical.com](https://support.lumerical.com)
- Lumerical 脚本参考：安装目录下 `scripting/`
- Ansys Learning Forum：[forum.ansys.com](https://forum.ansys.com)
- Ansys 2026 R1 Release Highlights：[ansys.com/products/release-highlights](https://www.ansys.com/products/release-highlights)

### 推荐学习路径

1. **入门**：完成 Lumerical 官方入门教程，熟悉 GUI 操作
2. **进阶**：掌握脚本编写、参数扫描、S参数提取
3. **高级**：MATLAB LiveLink 联合优化、自定义材料、高级后处理

### 开源替代

如果暂时无法获取 Lumerical 授权，可考虑开源 FDTD 工具：

- **MEEP**（MIT 开源 FDTD）：[meep.readthedocs.io](https://meep.readthedocs.io)，Python 接口，AI 对其支持很好
- **openFDTD**：较简单的开源实现

AI 可以帮你将 Lumerical 脚本转换为 MEEP Python 脚本，实现低成本替代。
