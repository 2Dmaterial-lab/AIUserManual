# SolidWorks：AI辅助三维建模与机械设计

> **本章导读**：按「简介与场景 → 安装配置 → AI 辅助技巧 → 示例与排错 → 进阶资源」组织，可按需跳读。

## 一、简介与适用场景

SolidWorks 是工业界最广泛使用的三维机械 CAD 软件之一。在物理与光学实验室中，它主要用于设计光路搭建的机械结构、仪器外壳、定制夹具以及加工件。与通用建模软件不同，SolidWorks 是参数化建模工具，每个尺寸都是可驱动、可修改的变量，这让它特别适合需要反复迭代的设计任务。

但 SolidWorks 的功能体系庞大，从草图绘制到零件建模、从装配配合到工程出图，完整的学习曲线相当陡峭。很多同学在实验室里只是偶尔用到，每次都要重新翻文档找操作方法，效率很低。AI 辅助可以在以下方面帮你提效：

- **建模策略指导**：描述你想设计的零件，AI 帮你规划建模顺序和特征选择，避免走弯路
- **宏录制与修改**：SolidWorks 支持 VBA 宏，AI 可以帮你生成宏代码实现批量操作自动化
- **工程图自动化**：批量出图、自动标注、BOM 表生成等重复性工作，用宏一键搞定
- **加工可行性检查**：向 AI 描述你的设计方案和加工方式，让它帮你检查壁厚、倒角、拔模等是否合理

### 典型使用场景

| 场景 | 传统做法 | AI 辅助做法 |
|------|----------|-------------|
| 设计光学元件安装座 | 凭经验选特征、反复试错 | 描述需求，AI 帮你规划建模步骤和特征组合 |
| 批量导出工程图 | 逐个打开零件、手动创建图纸 | AI 生成 VBA 宏，自动遍历零件并出图 |
| 装配体配合设计 | 手动逐个添加配合，容易遗漏 | AI 帮你梳理配合策略，给出配合方案 |
| 3D 打印前处理 | 凭感觉检查模型，经常打印失败 | AI 帮你检查壁厚、悬空面等常见问题 |

---

## 二、安装与配置

### 2.1 获取 SolidWorks

**推荐方案：SolidWorks 教育版**

SolidWorks 为在校学生提供免费的教育版许可，功能与商业版基本一致（仅部分高级插件受限）。

1. 访问 [SolidWorks 教育版页面](https://www.solidworks.com/zh/sw/education/solidworks-student-design-kit.html)，使用学校邮箱（.edu.cn 后缀）验证学生身份
2. 如果学校已购买校园教育版授权，请联系实验室老师或学校 IT 部门获取安装包和序列号
3. 下载 Student Design Kit 或 Education Edition 安装包

> 提示：教育版与商业版在建模核心功能上完全一致，可以放心用于实验室的设计工作。部分高级仿真插件（如 Flow Simulation）可能需要额外授权。

### 2.2 安装与激活

1. 运行安装程序，选择"单机安装"
2. 输入序列号（教育版通常是一年有效期，到期后需重新申请）
3. 安装类型选择"完整安装"，确保包含以下组件：
   - SolidWorks 基础功能
   - SolidWorks Toolbox（标准件库）
   - eDrawings（图纸查看器）
   - SolidWorks API SDK（宏开发所需，可选安装）
4. 安装完成后，首次启动需要在线激活

### 2.3 关键配置

安装完成后，做以下配置可以大幅提升使用效率：

**启用宏功能**（使用 VBA 自动化必需）：

1. 工具 -> 插件，勾选"SolidWorks Macro"，点击确定
2. 确认"宏"工具栏可见：视图 -> 工具栏 -> 勾选"宏"
3. 之后可以通过 工具 -> 宏 -> 运行 来执行宏文件

**加载常用插件**：

1. 工具 -> 插件，建议勾选以下插件：
   - SolidWorks Toolbox：标准螺栓、螺母、轴承等标准件库
   - SolidWorks Routing：管路设计（光路中有管道需求时有用）
   - Simulation：基础静力学分析（检查结构强度）

**设置文件模板**：

1. 新建零件时，选择"gb_part"模板（国标模板），确保单位为毫米、公差标准为中国标准
2. 如果模板列表中没有国标模板，可以手动设置：工具 -> 选项 -> 文件属性 -> 单位 -> 选择"MMGS（毫米、克、秒）"
3. 保存为模板：文件 -> 另存为 -> 文件类型选择"Part Templates (*.prtdot)"，保存到模板目录

**自定义快捷键**：

1. 工具 -> 自定义 -> 键盘
2. 建议为以下高频操作设置快捷键：
   - 拉伸凸台/基体：建议设为 `Ctrl+E`
   - 拉伸切除：建议设为 `Ctrl+Shift+E`
   - 保存：`Ctrl+S`（默认已有）
   - 撤销：`Ctrl+Z`（默认已有）
   - 重建模型：`Ctrl+Q`（默认已有，强制重建所有特征）

---

## 三、AI辅助使用核心技巧

### 3.1 用对话式AI规划建模策略

SolidWorks 建模的关键不是"怎么画"，而是"画什么先"。建模顺序决定了后续修改的难度和模型的稳定性。很多同学拿到一个零件就直接上手画，结果改一个尺寸整个模型就崩了，只能从头来过。

AI 可以帮你规划建模顺序。核心思路是：**先主体后细节，先对称后局部，先拉伸后切除**。

**向 AI 描述零件的要点**：

1. **说明零件的整体形状**：大致是一个什么几何体（长方体、圆柱体、L形等）
2. **说明关键功能特征**：有哪些孔、槽、台阶、螺纹等
3. **说明对称性**：是否关于某个平面对称
4. **说明加工方式**：是机加工还是 3D 打印，这影响倒角、壁厚等细节设计

### 3.2 用对话式AI编写VBA宏

SolidWorks 的 VBA 宏与 Excel 类似，但操作的是三维模型对象。AI 可以帮你生成完整的宏代码，实现批量出图、批量修改属性、自动导出等操作。

**编写 SolidWorks VBA 宏的流程**：

1. 用自然语言向 AI 描述你要自动化做什么
2. AI 生成 VBA 代码
3. 在 SolidWorks 中打开宏编辑器：工具 -> 宏 -> 新建，或编辑已有宏文件
4. 粘贴代码，修改路径等参数
5. 运行测试：工具 -> 宏 -> 运行，选择宏文件执行
6. 如果报错，把错误信息和出错行号发给 AI，让它帮你修复

**录制宏作为起点**：

1. 工具 -> 宏 -> 录制，然后手动执行你想自动化的操作
2. 操作完成后，工具 -> 宏 -> 停止，保存宏文件
3. 把录制的宏代码发给 AI，让它帮你优化、添加循环逻辑、增加错误处理

> 注意：录制宏是学习 SolidWorks API 最快的方式。录制的代码虽然不够优雅，但包含了正确的 API 调用方式，AI 可以在此基础上帮你改进。

### 3.3 AI辅助工程图标注

工程图是 SolidWorks 中最容易让人头疼的环节。标注繁琐、格式统一性要求高、重复操作多。AI 的辅助方式是：

- **标注策略指导**：告诉 AI 你的零件类型和加工要求，它帮你列出需要标注哪些尺寸、公差和表面粗糙度
- **批量标注宏**：对于标准结构的零件（如法兰、支架），AI 可以帮你生成自动标注的宏
- **BOM 表自动生成**：装配体工程图中，AI 帮你规划 BOM 表格式和属性映射

### 3.4 提问公式

无论什么场景，一个高效的提问通常包含以下要素：

```
[零件描述] + [设计要求] + [加工方式] + [SolidWorks版本]
```

例如：

> 我需要设计一个光学反射镜安装座，用来固定 2 英寸（直径50.8mm）的圆形反射镜。安装座是 L 形结构，底座通过 4 个 M4 螺栓固定在光学面包板上，竖直部分有一个圆形凹槽放置反射镜，用 M3 顶丝从侧面固定。材料为铝合金 6061，机加工。我使用的是 SolidWorks 2023 教育版。请帮我规划建模步骤。

---

## 四、常见任务与提示词示例

以下提示词可以直接复制使用，根据你的实际零件尺寸和要求修改参数即可。

### 任务1：光学安装座建模流程

**场景**：你需要设计一个用来固定光学元件的机械零件，但不确定应该先用什么特征、建模顺序怎么安排。

**提示词**：

> 请帮我规划以下零件在 SolidWorks 中的建模步骤：
> - 零件名称：光纤准直器安装座
> - 整体形状：L 形支架，底板 60mm x 40mm x 8mm，竖板 60mm x 30mm x 8mm
> - 底板上有 4 个 M4 通孔（用于固定到光学面包板），孔心距边缘 8mm，4 孔对称分布
> - 竖板中心有一个直径 12mm 的通孔（穿光纤准直器），孔两侧各有一个 M3 螺纹孔（顶丝固定用）
> - 底板和竖板之间有半径 5mm 的圆角过渡
> - 材料为铝合金 6061-T6，CNC 机加工
> - 零件关于前视基准面对称
>
> 请按操作步骤列出：
> 1. 选择哪个基准面绘制草图
> 2. 每一步使用什么特征（拉伸/切除/圆角等）
> 3. 每一步的关键尺寸
> 4. 需要注意的设计细节（如拔模角、最小壁厚等）

**预期建模步骤参考**：

1. **选择前视基准面**，绘制 L 形截面草图（利用对称关系，只画一半然后镜像）
2. **拉伸凸台**，两侧对称拉伸，深度 60mm（得到 L 形主体）
3. **选择底板下表面**，绘制 4 个 M4 通孔的位置草图（利用对称约束），**拉伸切除**，贯穿所有
4. **选择竖板侧面**，绘制直径 12mm 中心孔，**拉伸切除**，贯穿
5. 在同一表面绘制两个 M3 螺纹孔位置，**异型孔向导** -> M3 螺纹孔，深度 10mm
6. **圆角特征**，选择底板与竖板交线，半径 5mm
7. **倒角特征**，底板底面四边倒角 C1（机加工去毛刺）
8. 材料设置：铝合金 6061-T6

> 设计细节提示：M3 螺纹孔建议使用异型孔向导而非拉伸切除，这样可以在工程图中自动生成螺纹标注；底板 M4 通孔建议添加沉头孔（C4.5 x 90度），让螺栓头部齐平。

### 任务2：VBA宏批量导出工程图

**场景**：你有一个装配体和十几个零件，每个都需要导出 PDF 格式的工程图，手动逐个操作太耗时。

**提示词**：

> 请帮我写一个 SolidWorks VBA 宏，需求如下：
> - 宏的功能：批量将指定文件夹下所有 .slddrw 工程图文件导出为 PDF
> - 源文件夹路径：D:\Projects\OpticalSetup\Drawings
> - PDF 输出到同文件夹下的 PDF 子文件夹中（如果不存在则自动创建）
> - 导出设置：A3 图纸，1:1 比例，高质量（600 DPI）
> - 处理完成后弹窗显示"共导出 X 个 PDF 文件"
> - 如果某个文件导出失败，跳过并记录文件名，最后在消息框中一并显示
> - 请在代码中添加中文注释

**预期代码参考**：

```vba
Sub BatchExportPDF()
    ' 定义变量
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim nErrors As Long
    Dim nWarnings As Long
    Dim bRet As Boolean
    
    Dim sourceFolder As String
    Dim pdfFolder As String
    Dim drawFile As String
    Dim pdfFile As String
    Dim exportCount As Integer
    Dim failList As String
    
    ' 初始化
    Set swApp = Application.SldWorks
    sourceFolder = "D:\Projects\OpticalSetup\Drawings\"
    pdfFolder = sourceFolder & "PDF\"
    exportCount = 0
    failList = ""
    
    ' 检查并创建 PDF 输出文件夹
    If Dir(pdfFolder, vbDirectory) = "" Then
        MkDir pdfFolder
    End If
    
    ' 遍历文件夹中的 .slddrw 文件
    drawFile = Dir(sourceFolder & "*.slddrw")
    
    Do While drawFile <> ""
        ' 打开工程图文件（只读模式，不显示）
        Set swModel = swApp.OpenDoc6(sourceFolder & drawFile, swDocDRAWING, swOpenDocOptions_ReadOnly, "", nErrors, nWarnings)
        
        If Not swModel Is Nothing Then
            ' 构建 PDF 文件路径（将 .slddrw 替换为 .pdf）
            pdfFile = pdfFolder & Left(drawFile, Len(drawFile) - 7) & ".pdf"
            
            ' 设置导出选项
            bRet = swModel.Extension.SetUserPreferenceInteger(swUserPreferenceInteger_e.swPdfExportResolution, 0, 2) ' 2 = 高质量(600 DPI)
            
            ' 导出为 PDF
            bRet = swModel.Extension.SaveAs(pdfFile, swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, nErrors, nWarnings)
            
            If bRet Then
                exportCount = exportCount + 1
            Else
                failList = failList & drawFile & vbCrLf
            End If
            
            ' 关闭文件，不保存
            swApp.CloseDoc drawFile
        Else
            failList = failList & drawFile & " (打开失败)" & vbCrLf
        End If
        
        ' 获取下一个文件
        drawFile = Dir
    Loop
    
    ' 显示结果
    Dim msg As String
    msg = "共导出 " & exportCount & " 个 PDF 文件"
    If failList <> "" Then
        msg = msg & vbCrLf & vbCrLf & "以下文件导出失败：" & vbCrLf & failList
    End If
    MsgBox msg, vbInformation, "批量导出完成"
    
End Sub
```

### 任务3：装配体配合策略

**场景**：你需要将多个零件组装成完整的光路系统，但不确定配合类型的选择和添加顺序，容易出现过约束或欠约束的问题。

**提示词**：

> 我要在 SolidWorks 中装配一个光学平台系统，包含以下零件：
> 1. 光学面包板（600mm x 300mm x 12mm），底面作为装配基准
> 2. 反射镜安装座（已设计好的 L 形零件），底部有 4 个 M4 安装孔
> 3. 反射镜（直径 50.8mm，厚度 8mm 的圆柱体），放置在安装座的凹槽中
> 4. M4x12 螺栓 x 4（从 Toolbox 标准件库插入），固定安装座到面包板
> 5. M3x6 顶丝 x 2（从 Toolbox 插入），固定反射镜到安装座
>
> 请帮我制定配合策略：
> - 每个零件应该添加什么类型的配合（重合/同轴/距离/高级配合等）
> - 配合的添加顺序（先配合哪个零件、后配合哪个）
> - 哪些配合需要锁定、哪些需要留自由度
> - 如何避免过约束
> - 标准件（螺栓、顶丝）的配合技巧

**预期配合策略参考**：

**步骤1：面包板（基准件）**

面包板是整个装配的基础，插入后默认固定（不需要添加配合）。确认其位置：底面朝下，顶面与装配体的上视基准面重合。

**步骤2：反射镜安装座**

1. 安装座底面 与 面包板顶面 -> **重合配合**（确定高度）
2. 安装座一个 M4 孔轴线 与 面包板对应孔轴线 -> **同轴配合**（确定 XY 位置）
3. 安装座另一个 M4 孔轴线 与 面包板对应孔轴线 -> **同轴配合**（确定旋转，注意两个同轴配合即可完全定位，不需要再加角度配合）
4. 此时安装座完全约束，不要添加多余的配合

> 技巧：用两个孔的同轴配合而非一个孔+一个面来定位，这样后续调整位置时只需修改第一个同轴配合的距离偏移即可。

**步骤3：反射镜**

1. 反射镜圆柱面 与 安装座凹槽圆柱面 -> **同轴配合**（确定径向位置）
2. 反射镜底面 与 安装座凹槽底面 -> **重合配合**（确定轴向位置）
3. 此时反射镜只能绕轴线旋转（1个自由度），对于光学件这是合理的——角度位置由顶丝锁定

**步骤4：M4 螺栓（4个）**

使用 Toolbox 插入标准件后，对每个螺栓：
1. 螺栓圆柱面 与 面包板安装孔圆柱面 -> **同轴配合**
2. 螺栓头部底面 与 安装座底面 -> **重合配合**

> 技巧：4个螺栓配合方式相同，可以用"随配合复制"功能一次性完成：添加第一个螺栓的配合后，选中该螺栓，插入 -> 随配合复制，选择对应的孔即可快速完成其余3个。

**步骤5：M3 顶丝（2个）**

同理：同轴配合 + 重合配合。顶丝的旋入深度可以用**距离配合**控制，留一个可调的距离值。

### 任务4：3D打印模型准备

**场景**：你设计了一个零件需要用 FDM 3D 打印机制作，但不确定模型是否符合打印要求，需要检查和调整。

**提示词**：

> 我设计了一个光学实验用的样品支架，准备用 FDM 3D 打印机（PLA 材料）打印。模型信息如下：
> - 整体尺寸：80mm x 50mm x 40mm
> - 最小壁厚：1.2mm
> - 有一个悬空桥接结构，跨度 25mm，无支撑
> - 有 4 个 M3 热熔螺母安装孔（直径 5.4mm，深度 8mm）
> - 有一个竖直方向的圆孔，直径 8mm，深 30mm
> - 底面有一个深度 0.4mm 的文字凹槽
>
> 请帮我检查以下问题并给出修改建议：
> 1. 壁厚是否足够？PLA 打印的最小推荐壁厚是多少？
> 2. 悬空桥接结构是否需要添加支撑？有什么替代设计方案可以避免支撑？
> 3. 热熔螺母安装孔的直径是否合适？
> 4. 竖直圆孔打印时可能出现什么问题？
> 5. 底面文字凹槽能否正常打印？
> 6. 打印方向建议：哪个面朝下放置最合理？
> 7. 请给出 SolidWorks 中需要修改的具体操作步骤

**预期检查建议参考**：

1. **壁厚**：1.2mm 偏薄。PLA 推荐最小壁厚为 2mm（至少 2 条打印线宽，假设 0.4mm 喷嘴，5 条线宽 = 2.0mm）。建议将非关键位置的壁厚增加到 2mm 以上。在 SolidWorks 中：右键需要修改的特征 -> 编辑草图 -> 修改尺寸 -> 重建。

2. **悬空桥接**：25mm 跨度的无支撑桥接对 PLA 来说偏大，容易出现下垂。替代方案：在桥接下方添加 45 度斜撑（厚度 2mm），形成一个三角形支撑结构，这样不需要打印支撑且结构更稳固。在 SolidWorks 中：在桥接所在的草图平面绘制三角形轮廓，拉伸切除形成斜撑空间，或拉伸凸台添加斜撑。

3. **热熔螺母孔**：M3 热熔螺母外径一般为 4.6-5.0mm，孔径 5.4mm 合理（留 0.2-0.4mm 余量便于压入）。注意孔的顶部建议加一个 0.5mm 的倒角，方便螺母对准压入。

4. **竖直圆孔**：直径 8mm 的竖直孔在 FDM 打印中问题不大，但深 30mm 的孔内壁会有台阶纹路。如果孔需要配合精度，建议：打印后用 8mm 铰刀精铰，或孔径设计为 7.8mm 留出铰孔余量。

5. **底面文字凹槽**：0.4mm 深度可以打印，但底面朝下时凹槽会被封死。必须确保文字面朝上打印，或在切片软件中将文字面设为顶面。如果文字必须在底面，改为凸起文字（0.4mm 凸台），打印后贴在平台上即可。

6. **打印方向**：建议将最大平面（80mm x 50mm）朝下放置，这样层纹方向与零件受力方向垂直，结构强度最佳。文字面朝上。悬空桥接结构如果添加了斜撑，可以水平打印无需支撑。

### 任务5：批量修改零件自定义属性

**场景**：你的零件文件需要统一添加自定义属性（如材料、图号、设计者等），用于工程图标题栏自动填充和BOM表生成。手动逐个修改太费时。

**提示词**：

> 请帮我写一个 SolidWorks VBA 宏，需求如下：
> - 遍历指定文件夹下的所有 .sldprt 零件文件
> - 为每个零件添加以下自定义属性（如果已存在则更新）：
>   - "图号"：取文件名（不含扩展名）
>   - "材料"：从 SolidWorks 材料属性中读取，如果为空则设为"AL6061"
>   - "设计者"：设为"OpticsLab"
>   - "日期"：设为当前日期（格式 YYYY-MM-DD）
> - 文件夹路径：D:\Projects\OpticalSetup\Parts
> - 修改后保存并关闭文件
> - 完成后显示处理了多少个文件
> - 请在代码中添加中文注释

**预期代码参考**：

```vba
Sub BatchUpdateCustomProps()
    ' 定义变量
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swCustPropMgr As SldWorks.CustomPropertyManager
    Dim nErrors As Long
    Dim nWarnings As Long
    Dim partFolder As String
    Dim partFile As String
    Dim partName As String
    Dim materialName As String
    Dim processedCount As Integer
    
    ' 初始化
    Set swApp = Application.SldWorks
    partFolder = "D:\Projects\OpticalSetup\Parts\"
    processedCount = 0
    
    ' 遍历文件夹中的 .sldprt 文件
    partFile = Dir(partFolder & "*.sldprt")
    
    Do While partFile <> ""
        ' 打开零件文件
        Set swModel = swApp.OpenDoc6(partFolder & partFile, swDocPART, swOpenDocOptions_Silent, "", nErrors, nWarnings)
        
        If Not swModel Is Nothing Then
            ' 获取文件名（不含扩展名）作为图号
            partName = Left(partFile, Len(partFile) - 7)
            
            ' 获取材料属性
            materialName = swModel.MaterialIdName
            If materialName = "" Then
                materialName = "AL6061"
            Else
                ' MaterialIdName 返回格式可能为 "AL6061-SolidWorks Material"，提取材料名
                If InStr(materialName, "-") > 0 Then
                    materialName = Left(materialName, InStr(materialName, "-") - 1)
                End If
            End If
            
            ' 获取自定义属性管理器
            Set swCustPropMgr = swModel.Extension.CustomPropertyManager("")
            
            ' 添加或更新自定义属性
            swCustPropMgr.Add3 "图号", swCustomInfoText, partName, swCustomPropertyReplaceValue
            swCustPropMgr.Add3 "材料", swCustomInfoText, materialName, swCustomPropertyReplaceValue
            swCustPropMgr.Add3 "设计者", swCustomInfoText, "OpticsLab", swCustomPropertyReplaceValue
            swCustPropMgr.Add3 "日期", swCustomInfoText, Format(Date, "yyyy-mm-dd"), swCustomPropertyReplaceValue
            
            ' 保存文件
            swModel.Save3 swSaveAsOptions_e.swSaveAsOptions_Silent, nErrors, nWarnings
            
            ' 关闭文件
            swApp.CloseDoc partFile
            
            processedCount = processedCount + 1
        End If
        
        ' 获取下一个文件
        partFile = Dir
    Loop
    
    ' 显示结果
    MsgBox "共处理 " & processedCount & " 个零件文件", vbInformation, "批量更新完成"
    
End Sub
```

---

## 五、常见问题与排错

### Q1：AI 给出的建模步骤中提到了某个特征，但我在 SolidWorks 中找不到

**原因**：SolidWorks 不同版本的功能位置有差异，部分特征名称在中英文版之间也有翻译差别。

**解决方法**：
- 告诉 AI 你使用的 SolidWorks 版本号和语言（中文版/英文版），让它给出对应的位置
- 使用 SolidWorks 的搜索功能：在右上角的搜索框中输入特征名称（中英文均可），可以直接跳转到对应命令
- 常见特征名称中英对照：拉伸凸台 = Extrude Boss/Base，拉伸切除 = Extruded Cut，旋转凸台 = Revolve Boss/Base，异型孔向导 = Hole Wizard

### Q2：VBA 宏运行时报"对象变量未设置"错误

**原因**：SolidWorks VBA 宏中最常见的错误，通常是因为打开文件失败或获取对象失败后继续操作。

**解决方法**：
- 检查文件路径是否正确，路径中的反斜杠 `\` 是否完整
- 在代码中添加空值检查，例如在 `OpenDoc6` 之后加上 `If swModel Is Nothing Then` 的判断
- 把完整的错误提示和代码发给 AI，让它帮你添加错误处理逻辑。一个健壮的宏应该在每个关键操作后都检查返回值
- 确认宏代码中引用了 SolidWorks 类型库：在 VBA 编辑器中，工具 -> 引用，勾选"SldWorks 20XX Type Library"

### Q3：装配体配合报"过约束"或"找不到解"

**原因**：添加的配合之间存在冲突，最常见的情况是同轴配合+距离配合+角度配合同时添加，自由度已经被完全消除后还继续添加配合。

**解决方法**：
- 在添加配合前，先计算自由度：每个零件有 6 个自由度（3 个平移 + 3 个旋转），每个配合会消除若干自由度
- 常见配合的约束数量：重合配合消除 1 个平移 + 2 个旋转（3个自由度），同轴配合消除 2 个平移 + 2 个旋转（4个自由度），距离配合消除 1 个平移（1个自由度）
- 如果出现过约束，在配合树中找到带警告标记的配合，右键删除多余配合
- 向 AI 描述你的装配体结构，让它帮你重新规划配合方案，避免冲突

### Q4：工程图中尺寸标注位置混乱，手动调整太麻烦

**原因**：SolidWorks 自动插入的尺寸位置往往不够理想，尤其是复杂零件。这是 SolidWorks 的通病，不是你的操作问题。

**解决方法**：
- 使用"模型项目"功能自动插入尺寸后，逐个拖动调整位置。虽然繁琐，但这是最可控的方式
- 对于需要频繁出图的标准化零件，可以让 AI 帮你编写宏来自动调整尺寸位置
- 在模型创建阶段就注意草图的尺寸放置位置，SolidWorks 在工程图中会尽量保留原始草图的尺寸布局
- 如果标注实在太乱，可以删除所有自动标注，手动使用"智能尺寸"逐个添加，虽然费时但最整洁

### Q5：3D 打印的零件尺寸偏差大，孔径偏小

**原因**：FDM 打印存在收缩和挤出宽度误差，孔径通常偏小 0.2-0.4mm，外轮廓偏大 0.1-0.3mm。

**解决方法**：
- 在 SolidWorks 中对需要配合的尺寸预留公差补偿：孔径加大 0.3mm，轴径减小 0.2mm
- 如果使用的是同一台打印机，建议先打印一个测试件（含不同直径的孔和不同尺寸的轴），测量实际偏差后建立补偿值表
- 向 AI 描述你的打印机和材料参数，让它帮你计算补偿量
- 对于高精度配合孔，建议在 SolidWorks 中按理论尺寸建模，打印后用铰刀或钻头精加工

### Q6：宏代码在别人的电脑上运行报错

**原因**：文件路径不同、SolidWorks 版本不同、缺少引用库等。

**解决方法**：
- 路径问题：把硬编码的路径改为让用户选择文件夹。在宏开头添加文件夹选择对话框：

```vba
' 弹出文件夹选择对话框
Dim shellApp As Object
Set shellApp = CreateObject("Shell.Application")
Dim selectedFolder As Object
Set selectedFolder = shellApp.BrowseForFolder(0, "请选择零件所在文件夹", 0)
If selectedFolder Is Nothing Then Exit Sub
partFolder = selectedFolder.Self.Path & "\"
```

- 版本问题：在代码中使用晚期绑定而非早期绑定，避免版本相关的引用问题。代价是失去代码自动补全，但兼容性更好
- 把错误信息发给 AI，它会帮你针对性修复

---

## 六、进阶资源

### 学习资源

- **SolidWorks 官方教程**：帮助 -> SolidWorks 教程，内置从入门到进阶的完整教程，建议至少完成"零件"和"装配体"两个模块
- **SolidWorks API 帮助**：在 VBA 编辑器中按 F1，或访问 [help.solidworks.com](https://help.solidworks.com/)，搜索"API"可以找到所有接口文档
- **SolidWorks 论坛**：[forum.solidworks.com](https://forum.solidworks.com/) 有大量实际问题的解决方案，遇到疑难杂症时先在这里搜索

### 进阶技巧

- **配置与设计表**：SolidWorks 的配置功能可以用一个零件文件管理多个变体（如不同长度的支架），配合 Excel 设计表可以实现参数化驱动。可以让 AI 帮你生成设计表的模板
- **焊件结构**：设计光学面包板上的支架时，使用焊件功能（结构构件 + 剪裁/延伸）比逐个拉伸更高效，AI 可以帮你选择合适的型材截面和节点处理方式
- **运动仿真**：如果装配体中有运动机构（如可调角度的反射镜架），使用 SolidWorks Motion 可以进行运动学分析，AI 可以辅助设置运动副和驱动参数
- **Simulation 静力分析**：对关键承载零件进行强度校核，AI 帮你选择分析类型、设置网格密度和边界条件

### 与 AI 协作的最佳实践

1. **先建后改**：让 AI 帮你规划建模策略后，先按方案完成主体建模，确认无误后再添加细节特征。不要一步到位——越复杂的模型，一步出错的概率越高
2. **保留设计意图**：在提问时说明哪些尺寸是固定的、哪些可能需要调整，AI 会据此帮你规划特征的依赖关系，让后续修改更容易
3. **录制宏再优化**：先手动录制宏获取正确的 API 调用，再让 AI 帮你添加循环、条件判断、错误处理等逻辑，比让 AI 从零写宏更可靠
4. **保存好宏文件**：把你验证过可用的宏文件统一保存在一个文件夹中，按功能命名（如 BatchExportPDF.swp、UpdateCustomProps.swp），下次直接使用
5. **逐步迭代**：如果 AI 给的建模方案不理想，不要从头重问，而是指出具体问题让它在原方案基础上修改，比如"第二步的拉伸切除改为旋转切除，因为孔是阶梯孔"
