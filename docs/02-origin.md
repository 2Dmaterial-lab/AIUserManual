# Origin — AI辅助使用指南

## 1. 简介与适用场景

Origin 是 OriginLab 公司开发的数据分析和绘图软件，在物理、化学、材料等领域的论文中几乎无处不在。课题组中 Origin 主要用于：

- **数据处理**：光谱分析、基线校正、平滑滤波
- **科学绘图**：publication 级别的多面板图、多轴图
- **曲线拟合**：非线性拟合、自定义函数拟合
- **批量分析**：对多组数据重复相同的分析流程
- **数据管理**：工作表管理、数据导入导出

## 2. 安装与配置

### 获取方式

- **学校授权**：多数高校有 Origin 的校园授权，通过学校软件下载平台获取
- **学生版**：OriginLab 提供学生版（功能完整，6个月免费），访问 [originlab.com/student](https://www.originlab.com/student)
- **试用版**：21天全功能试用

### 安装要点

- 选择 64-bit 版本
- 安装时选择需要的 App（Origin 内置的应用商店），推荐安装：
  - Batch Processing App
  - 2D Bin Plot App
  - Heat Map with Dendrogram App
- 配置默认绘图模板：`Preferences → System Paths → User Files`

### 推荐配置

1. **设置默认字体**：`Preferences → System Variables`，添加 `@FNT=Helvetica`
2. **设置默认图模板**：右键某个图 → `Save Template as...`
3. **自动保存**：`Preferences → Options → Open/Close → Auto Save interval: 5 min`
4. **Python 支持**：Origin 2023+ 内置 Python，可在 Script Window 中直接使用

## 3. AI辅助使用核心技巧

### 对话式AI（Claude/ChatGPT/DeepSeek）

Origin 与 AI 配合的核心方式：

#### 生成 LabTalk 脚本

Origin 有自己的脚本语言 LabTalk，AI 可以帮你生成各种自动化脚本：

- **批量导入数据**：指定文件格式和导入规则，AI 生成 LabTalk 脚本
- **批量出图**：描述图的类型和格式要求，AI 生成绘图脚本
- **批量拟合**：指定拟合函数和参数，AI 生成拟合脚本
- **数据操作**：列运算、筛选、排序的脚本

#### 利用 Python 接口

Origin 2021+ 支持 `originpro` Python 包，可以直接用 Python 控制 Origin：

- AI 生成 Python 代码比 LabTalk 更可靠（Python 是主流语言）
- 可以在 Jupyter Notebook 中远程控制 Origin
- 适合复杂的数据处理流程

#### 常规问答

- 报错信息解读
- 特定功能的操作步骤
- 图表格式设置方法

## 4. 常见任务与提示词示例

### 场景1：批量从CSV文件绘图

**提示词**：

> 我有一个文件夹中有20个CSV文件，文件名格式为 sample_01.csv 到 sample_20.csv。每个CSV有两列：第一列是波长(nm)，第二列是透过率(%)。
>
> 请帮我写一个 Origin LabTalk 脚本，完成以下操作：
> 1. 批量导入所有CSV文件到同一个工作簿的不同工作表
> 2. 每个工作表自动命名为对应的文件名
> 3. 对每个工作表画出线图（波长 vs 透过率）
> 4. 所有图合并到一个 Graph 中
> 5. 统一设置：x轴范围400-800nm，y轴范围0-100%，线宽1.5pt，黑色线条

**预期输出**：LabTalk 脚本

```labtalk
// 批量导入CSV并绘图
// 在 Script Window 中运行

// 定义文件夹路径
string path$ = "C:\Data\Samples\";

// 获取文件列表
findfiles fname:=path$ + "*.csv";

// 循环导入
int sheetIndex = 1;
doc -e W {
    // 导入CSV
    impCSV fname:=%(path$) delimiter:=comma;
    // 重命名工作表
    page.active = sheetIndex;
    wks.name$ = "Sample%Z"; // 自动编号
    sheetIndex++;
}

// 绘制所有数据到同一图
plotxy iy:=(1,2) plot:=200; // 线图
doc -e W {
    plotxy iy:=%(@W,1,2) plot:=200 ogl:=[Graph1]1!;
}

// 设置轴范围和样式
layer.x.from = 400;
layer.x.to = 800;
layer.y.from = 0;
layer.y.to = 100;
set %C -lw 1.5;
```

**Python 版本（推荐）**：

```python
import originpro as op
import glob

# 批量导入CSV
app = op.Application()
files = sorted(glob.glob(r'C:\Data\Samples\*.csv'))

# 创建工作簿
wb = op.new_book()
for i, f in enumerate(files):
    wks = wb[i] if i < wb.count else wb.add_sheet()
    wks.from_file(f, False)  # 导入CSV

# 创建图
gp = op.new_graph()
for i in range(len(files)):
    wks = wb[i]
    plot = gp[0].add_plot(wks, colx=0, coly=1, type='line')

# 格式设置
gp[0].set_xlim(400, 800)
gp[0].set_ylim(0, 100)
gp[0].axis('x').label='Wavelength (nm)'
gp[0].axis('y').label='Transmittance (%)'
```

### 场景2：非线性曲线拟合

**提示词**：

> 我在 Origin 中有一组透过率光谱数据，需要用洛伦兹函数拟合。自定义拟合函数为：
> y = y0 + A * (w/2)^2 / ((x-xc)^2 + (w/2)^2)
> 其中 y0 是基线，A 是振幅，xc 是中心位置，w 是FWHM。
>
> 请告诉我：
> 1. 如何在 Origin 中创建自定义拟合函数
> 2. 设置初始参数值的建议
> 3. 如何用脚本进行批量拟合
> 4. 如何将拟合结果导出到工作表

**预期输出**：详细的操作步骤 + LabTalk 脚本

**步骤1：创建自定义拟合函数**

1. `Analysis → Fitting → Nonlinear Curve Fit → Open Dialog`
2. 选择 `Create a new function`
3. 函数名：`Lorentzian`，选择 `User Defined`
4. 参数：`y0, A, xc, w`
5. 函数体：
```
y0 + A * (w/2)^2 / ((x-xc)^2 + (w/2)^2)
```
6. 参数初始值：`y0=0, A=1, xc=1550, w=10`

**步骤2：批量拟合脚本**

```labtalk
// 批量洛伦兹拟合
// 假设每个工作表的数据在第1、2列
doc -e W {
    // 对当前工作表的第1、2列进行拟合
    nlbegin iy:=(1,2) func:=Lorentzian nltree:=tt;
    // 设置初始值
    tt.y0 = 0;
    tt.A = 1;
    tt.xc = 1550;
    tt.w = 10;
    // 执行拟合
    nlfit;
    // 输出结果
    nlend;
}
```

### 场景3：Publication级别图表设置

**提示词**：

> 我需要在 Origin 中制作一张符合 Nature/Science 级别期刊要求的图表，要求：
> - 双Y轴图（左轴透过率，右轴反射率）
> - 字体：Helvetica，8pt（适用于单栏图）
> - 线宽：坐标轴线0.5pt，数据线1.5pt
> - 刻度朝内
> - 无上边框和右边框
> - 图例无边框
> - 输出为300dpi TIFF格式
> - 图片宽度8.9cm（Nature单栏宽度）
>
> 请给我详细的操作步骤或LabTalk脚本。

**预期输出**：格式设置脚本

```labtalk
// 设置图的格式为出版标准
// 假设当前活动图窗口为 Graph1

// 页面尺寸
page.width = 8.9;   // cm
page.height = 6;     // cm

// 左Y轴
layer.y.from = 0;
layer.y.to = 100;
layer.y.label.font = font(Helvetica);
layer.y.label.pt = 8;
layer.y.tickLen = 2;    // 刻度长度
layer.y.tickSide = 1;   // 刻度朝内
layer.y.axis = 1;       // 只显示左边轴

// 右Y轴
layer2.y.from = 0;
layer2.y.to = 50;
layer2.y.label.font = font(Helvetica);
layer2.y.label.pt = 8;

// X轴
layer.x.from = 400;
layer.x.to = 800;
layer.x.label.font = font(Helvetica);
layer.x.label.pt = 8;
layer.x.tickLen = 2;
layer.x.tickSide = 1;

// 隐藏上边框和右边框
layer.x.showAxis = 1;  // 只显示下轴
layer.x.showTicks = 1;

// 图例设置
legend.background = 0;  // 无边框
legend.fsize = 8;

// 数据线宽
set %C -lw 1.5;

// 导出TIFF
expGraph type:=tiff dpi:=300 width:=8.9 units:=cm;
```

### 场景4：数据导出自动化

**提示词**：

> 我在 Origin 中有一个包含10个工作表的工作簿，每个工作表有三列数据。我需要：
> 1. 将每个工作表导出为单独的 CSV 文件
> 2. 文件名与工作表名相同
> 3. 同时导出每个工作表对应的图为 PNG 图片
>
> 请用 originpro Python 包写一个脚本。

**预期输出**：Python 脚本

```python
import originpro as op

# 获取当前活动工作簿
wb = op.find_book('w', active=True)
if wb is None:
    wb = op.new_book()

# 遍历所有工作表
for i in range(wb.count):
    wks = wb[i]
    sheet_name = wks.name

    # 导出CSV
    csv_path = f'C:\\Data\\Export\\{sheet_name}.csv'
    wks.to_file(csv_path, False)  # False = 不带列标题格式

    # 创建对应的图
    gp = op.new_graph(template='Line')
    plot = gp[0].add_plot(wks, colx=0, coly=1, type='line')

    # 导出PNG
    png_path = f'C:\\Data\\Export\\{sheet_name}.png'
    gp.save_png(png_path, dpi=300, width=8.9)

    # 关闭图窗口
    gp.destroy()

print(f'导出完成: {wb.count} 个工作表')
```

## 5. 常见问题与排错

### AI能帮你快速解决的问题

| 问题 | AI协助方式 |
|------|-----------|
| LabTalk 语法不清楚 | 描述功能需求，AI 生成脚本 |
| 绘图格式调整 | 描述目标样式，AI 给出设置命令 |
| 数据导入问题 | 说明文件格式，AI 给出导入参数 |
| 批量操作 | 描述重复性任务，AI 生成循环脚本 |
| 拟合函数定义 | 给出数学表达式，AI 转换为 Origin 格式 |

### 需要注意的事项

- **LabTalk 版本差异**：不同版本的 Origin 的 LabTalk 语法有差异，AI 生成的脚本可能需要微调
- **Python vs LabTalk**：复杂任务优先用 `originpro` Python 包，AI 对 Python 更熟悉
- **路径问题**：LabTalk 中的路径使用反斜杠 `\`，注意转义
- **中文列名**：如果列名含中文，脚本中可能需要特殊处理

### 常见问题速查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 脚本运行报错"undefined variable" | 变量未定义 | 检查变量名拼写和作用域 |
| 导入CSV格式错乱 | 分隔符设置不对 | `impCSV` 时指定 `delimiter:=comma` |
| 图例显示不全 | 图例区域太小 | 双击图例手动调整大小 |
| 批量操作只对第一个有效 | 循环语法错误 | 使用 `doc -e W {}` 遍历工作表 |
| Python 报错找不到 originpro | Python 环境不对 | 在 Origin 内置 Python 中安装：`pip install originpro` |

## 6. 进阶资源

### 官方资源

- Origin 官方文档：[originlab.com/doc](https://www.originlab.com/doc)
- LabTalk 脚本参考：[originlab.com/doc/LabTalk](https://www.originlab.com/doc/LabTalk)
- originpro Python 包文档：[originlab.com/doc/python](https://www.originlab.com/doc/python)
- Origin 视频教程：[originlab.com/videos](https://www.originlab.com/videos)

### 推荐学习路径

1. **入门**：掌握基本绘图操作、数据导入、图层管理
2. **进阶**：学习 LabTalk 脚本、自定义拟合函数、批量处理
3. **高级**：使用 originpro Python 包进行复杂自动化、创建自定义 App

### 实用技巧

- 保存常用图为模板：右键图窗口 → `Save Template as...`
- 用 `Script Window` 快速测试 LabTalk 命令
- 按 `Ctrl+Shift+H` 查看当前图的所有对象层级
- 用 `Analysis → Batch Processing` 进行批量分析（GUI 方式）
