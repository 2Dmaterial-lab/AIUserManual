# Excel：AI辅助数据处理与可视化

> **本章导读**：按「简介与场景 → 安装配置 → AI 辅助技巧 → 示例与排错 → 进阶资源」组织，可按需跳读。

!!! info "版本与功能时效"

    本章按 Microsoft 365/Excel 2026 年前后的公开功能和常见科研数据处理需求整理。Copilot、Power Query、动态数组函数和网页版能力会随许可证变化；请以学校账号实际可用功能为准。

## 1. 简介与适用场景

Excel 是科研中最常用的数据处理与可视化工具之一。无论你是整理实验数据、生成统计报表，还是制作可视化图表，Excel 都能胜任。但说实话，很多同学对 Excel 的掌握停留在"手动输入公式 + 拖拽填充"的阶段，遇到复杂需求就束手无策。

AI 辅助可以帮你跨越这个门槛：

- **公式生成**：描述你想要的结果，AI 帮你写出复杂嵌套公式，不用再一个个函数去查
- **VBA 宏编写**：不会 VBA 也能批量处理数据，AI 帮你生成完整的宏代码
- **数据透视表**：告诉 AI 你的分析目标，它帮你规划字段布局和计算方式
- **Power Query 数据清洗**：面对杂乱的原始数据，AI 帮你设计清洗流程

### 典型使用场景

| 场景 | 传统做法 | AI 辅助做法 |
|------|----------|-------------|
| 实验数据整理 | 手动复制粘贴、逐个设公式 | 描述需求，AI 生成公式或 VBA 宏一键处理 |
| 自动生成报告 | 每次手动更新数据和图表 | AI 帮写 VBA 宏自动刷新报表 |
| 条件格式标记 | 在菜单里翻找设置项 | 描述规则，AI 给出完整设置步骤和公式 |
| 数据清洗 | 逐列检查、手动删除异常值 | AI 帮你设计 Power Query 清洗流程 |

### 什么时候优先用 Excel

| 场景 | 建议 | 原因 |
|------|------|------|
| 小规模数据查看、筛选、人工标注 | 推荐 | 上手快，适合临时整理 |
| 组内共享表格、报销、样品台账 | 推荐 | 协作和表格格式友好 |
| 重复清洗同格式文件 | 推荐 Power Query / VBA | 可把操作步骤保存下来 |
| 论文最终数据分析链 | 谨慎 | 必须保留公式、Power Query 和校验记录 |
| 大规模数值计算和复杂统计 | 不优先 | MATLAB/Python 更可复现、更容易测试 |

### AI 能做 / 不能做

| AI 适合做 | 必须人工确认 |
|-----------|--------------|
| 生成公式、VBA、Power Query M 代码 | 公式引用区域是否正确 |
| 解释函数、数据透视表和条件格式 | 文本数字、日期格式和空值处理 |
| 用 Copilot 做表内辅助分析 | 结果是否可复现、是否适合科研结论 |
| 设计报表字段和清洗流程 | 宏是否覆盖原始数据 |

### 最小闭环案例

1. 复制一份小型 CSV 到测试工作簿。
2. 让 AI 生成公式或 Power Query 步骤，完成筛选、单位换算和汇总。
3. 用 3 行数据手算校验结果。
4. 保存测试副本、公式说明和导出的处理后表格。

---

## 2. 安装与配置

### 2.1 获取 Excel

**可选方案：Microsoft 365 学生/校园授权**

1. 访问 [Microsoft 教育版页面](https://www.microsoft.com/zh-cn/education/products/office)，输入学校邮箱（.edu.cn 后缀），验证学生身份后可免费使用网页版 Office，或以优惠价格订阅桌面版
2. 如果学校已购买校园授权，直接用学校账号登录 [office.com](https://www.office.com) 即可下载安装

**替代方案**：
- WPS Office：免费，界面与 Excel 兼容，但部分高级功能（Power Query、部分 VBA）支持有限
- LibreOffice Calc：完全免费开源，VBA 兼容性较差，不推荐用于复杂自动化任务

> 提示：如果需要 Power Query、VBA、批量导入导出或插件，桌面版 Excel 通常比网页版更完整；只做简单查看和协作时网页版也够用。

### 2.2 关键配置

安装完成后，做以下配置可以大幅提升使用效率：

**启用开发工具选项卡**（使用 VBA 必需）：
1. 文件 -> 选项 -> 自定义功能区
2. 勾选"开发工具"，点击确定
3. 之后可以在"开发工具"选项卡中录制宏、打开 VBA 编辑器

**启用 Power Query**（Office 365 默认已集成）：
1. 在"数据"选项卡中可以看到"获取数据"按钮，说明 Power Query 已可用
2. 如果看不到，检查 Office 更新：文件 -> 账户 -> 更新选项 -> 立即更新

**常用快捷设置**：
1. 文件 -> 选项 -> 公式 -> 勾选"启用迭代计算"（某些循环引用公式需要）
2. 文件 -> 选项 -> 高级 -> 取消勾选"自动完成单元格值"（避免输入时自动填充干扰）
3. 文件 -> 选项 -> 保存 -> 设置自动保存间隔为 5 分钟

### 2.3 Copilot for Excel（如可用）

如果你的 Microsoft 365 许可证包含 Copilot，你会在 Excel 功能区看到 Copilot 入口。Copilot 可以直接在 Excel 中用自然语言辅助操作，比如"高亮大于平均值的数据"、"添加一列计算同比增长率"等。

Copilot for Excel 的能力和入口在 2026 年仍在调整，部分 App Skills 和 Office 内嵌入口会随许可证变化。对于复杂 VBA、Power Query M 代码和可复现数据处理，仍建议让对话式 AI 生成可审查的公式/脚本，再由你手动验证。

!!! warning "数据安全"

    不要把未发表实验数据、专利相关信息或包含个人信息的工作簿上传到云端 AI。需要借助 AI 调试公式时，优先使用脱敏后的列名和少量模拟数据。

---

## 3. AI辅助使用核心技巧

### 3.1 用对话式AI生成公式

Excel 有几百个函数，没人能全记住。关键是学会向 AI 描述你的需求，让它帮你找到合适的函数组合。

**描述公式的要点**：

1. **说明数据位置**：告诉 AI 你的数据在哪几列、表头是什么
2. **说明计算逻辑**：用自然语言描述你想要的结果，不需要知道用什么函数
3. **说明特殊情况**：有没有空值？有没有错误值需要处理？需不需要忽略某些行？

**示例对话**：

> 我的数据在 A 列到 E 列，A 列是样品编号，B 列是测量日期，C 列是温度，D 列是湿度，E 列是测量值。我想在 F 列计算每个样品的测量值与该日期所有样品平均值的偏差百分比，忽略 E 列中的空值。

AI 会返回类似这样的公式：

```excel
=IF(E2="","", (E2 - AVERAGEIF(B:B, B2, E:E)) / AVERAGEIF(B:B, B2, E:E) * 100)
```

你只需要复制粘贴到 F2 单元格，然后向下填充即可。

### 3.2 用对话式AI编写VBA宏

VBA 是 Excel 自动化的核心能力，但学习曲线陡峭。AI 可以帮你跨过这道坎。

**编写 VBA 宏的流程**：

1. 用自然语言向 AI 描述你要做什么
2. AI 生成 VBA 代码
3. 复制到 VBA 编辑器（Alt + F11 打开）
4. 运行测试（F5 运行，或在 Excel 中通过开发工具 -> 宏 -> 运行）
5. 如果报错，把错误信息发给 AI，让它帮你修复

**注意事项**：
- 始终在测试数据上先运行宏，确认无误后再用于正式数据
- 重要数据在运行宏之前先备份（另存为副本）
- 如果 AI 生成的代码运行报错，把完整的错误提示和出错的那行代码发给 AI，它能精准定位问题

### 3.3 AI辅助数据透视表与Power Query

数据透视表和 Power Query 的操作比较图形化，AI 辅助的方式是帮你规划操作步骤：

- **数据透视表**：向 AI 描述你的分析维度和指标，它会告诉你行字段、列字段、值字段分别放什么，以及用什么汇总方式
- **Power Query**：向 AI 描述数据清洗需求，它帮你生成 M 语言代码，你可以直接粘贴到 Power Query 的高级编辑器中

### 3.4 AI 生成公式/宏的验收清单

1. **先复制工作簿**：VBA 宏执行后通常无法撤销，先另存为测试副本。
2. **检查函数兼容性**：确认是否使用 `XLOOKUP`、`FILTER`、`UNIQUE`、`LET`、`LAMBDA` 等新版函数。
3. **用手算样例验证**：挑 3–5 行数据手算，核对公式结果。
4. **保留清洗步骤**：Power Query 的 M 代码比手工操作更可复现，建议保存在工作簿或单独 `.pq` 文本中。
5. **避免覆盖原始数据**：宏输出到新工作表或新文件，原始数据只读。

### 3.5 提问公式

无论什么场景，一个高效的提问通常包含以下要素：

```
[数据情况] + [目标结果] + [约束条件] + [工具版本]
```

例如：

> 我的 Excel 表格有 5000 行数据，A 列是日期格式 YYYY-MM-DD，B 列是实验组名称（共3组：control、treatment-A、treatment-B），C 列到 F 列是四项检测指标的数值。我需要：1) 在 G 列生成每行数据的综合评分，四项指标的权重分别是 0.3、0.2、0.3、0.2；2) 用条件格式标出综合评分前 10% 的行。我使用的是 Office 365 版 Excel。

---

## 4. 常见任务与提示词示例

以下提示词可以直接复制使用，根据你的实际数据情况修改列号、表名等参数即可。

### 任务1：复杂公式生成

**场景**：你有一组实验数据，需要根据多个条件进行统计计算，手动写公式很容易出错。

**提示词**：

> 请帮我写一个 Excel 公式，需求如下：
> - 数据表名为 Sheet1，A 列是实验日期（格式 2025-03-15），B 列是样品组别（A组/B组/C组），C 列是测量值（数值），D 列是是否合格（是/否）
> - 我需要在另一个 Sheet2 的 A1 单元格计算：2025年3月份、B组、合格样品的测量值平均值，结果保留两位小数
> - 如果没有符合条件的数据，显示"无数据"而不是报错
> - 请解释公式中每个函数的作用

**预期输出参考**：

```excel
=IFERROR(ROUND(AVERAGEIFS(Sheet1!C:C, Sheet1!A:A, ">=2025-03-01", Sheet1!A:A, "<=2025-03-31", Sheet1!B:B, "B组", Sheet1!D:D, "是"), 2), "无数据")
```

函数说明：
- `AVERAGEIFS`：多条件平均，同时满足日期范围、组别、合格三个条件
- `ROUND(..., 2)`：保留两位小数
- `IFERROR`：当没有匹配数据时（AVERAGEIFS 返回 #DIV/0! 错误），显示"无数据"

### 任务2：VBA宏批量处理

**场景**：你有几十个结构相同的工作表，需要逐个执行相同的处理操作。

**提示词**：

> 请帮我写一个 Excel VBA 宏，需求如下：
> - 工作簿中有多个工作表，名称格式为 "Sample_01" 到 "Sample_30"
> - 每个工作表结构相同：A 列是时间（秒），B 列是温度读数，C 列是压力读数
> - 我需要宏自动完成以下操作：
>   1. 在每个工作表的 D 列计算温度变化率（当前行温度减去上一行温度，除以时间差）
>   2. 在每个工作表的 E 列标注压力是否超限（压力 > 100 时标"超限"，否则标"正常"）
>   3. 在每个工作表的 F1 单元格写入该表最高温度及对应时间
>   4. 第一行是表头，从第二行开始处理数据
> - 处理完成后弹出一个消息框显示"30个工作表处理完成"
> - 请在代码中添加中文注释，方便我理解

**预期输出参考**：

```vba
Sub BatchProcessSamples()
    Dim ws As Worksheet
    Dim i As Long
    Dim lastRow As Long
    Dim maxTemp As Double
    Dim maxTempTime As Double
    Dim processedCount As Integer

    processedCount = 0

    ' 遍历所有工作表
    For Each ws In ThisWorkbook.Worksheets
        ' 只处理名称以 "Sample_" 开头的工作表
        If Left(ws.Name, 7) = "Sample_" Then
            ' 添加表头
            ws.Cells(1, 4).Value = "温度变化率"
            ws.Cells(1, 5).Value = "压力状态"
            ws.Cells(1, 6).Value = "最高温度及时间"

            ' 获取最后一行数据
            lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

            ' 初始化最高温度
            maxTemp = ws.Cells(2, 2).Value
            maxTempTime = ws.Cells(2, 1).Value

            ' 从第二行开始处理数据
            For i = 2 To lastRow
                ' 计算温度变化率
                If i = 2 Then
                    ws.Cells(i, 4).Value = "N/A"  ' 第一行数据没有前一行，无法计算变化率
                Else
                    Dim timeDiff As Double
                    timeDiff = ws.Cells(i, 1).Value - ws.Cells(i - 1, 1).Value
                    If timeDiff <> 0 Then
                        ws.Cells(i, 4).Value = (ws.Cells(i, 2).Value - ws.Cells(i - 1, 2).Value) / timeDiff
                    Else
                        ws.Cells(i, 4).Value = "N/A"
                    End If
                End If

                ' 标注压力状态
                If ws.Cells(i, 3).Value > 100 Then
                    ws.Cells(i, 5).Value = "超限"
                Else
                    ws.Cells(i, 5).Value = "正常"
                End If

                ' 记录最高温度及其对应时间
                If ws.Cells(i, 2).Value > maxTemp Then
                    maxTemp = ws.Cells(i, 2).Value
                    maxTempTime = ws.Cells(i, 1).Value
                End If
            Next i

            ' 写入最高温度信息
            ws.Cells(1, 6).Value = "最高温度: " & maxTemp & " (时间: " & maxTempTime & "s)"

            processedCount = processedCount + 1
        End If
    Next ws

    ' 完成提示
    MsgBox processedCount & "个工作表处理完成", vbInformation, "处理结果"
End Sub
```

### 任务3：数据透视表设置指导

**场景**：你需要从原始实验记录中快速汇总分组统计数据。

**提示词**：

> 我有一张实验数据表，列结构如下：
> - A列：实验日期
> - B列：实验人员（张三/李四/王五）
> - C列：样品类型（Type1/Type2/Type3）
> - D列：测量值1
> - E列：测量值2
> - F列：是否合格（合格/不合格）
>
> 我想创建一个数据透视表，实现以下分析：
> 1. 按实验人员和样品类型交叉统计合格率（合格数/总数）
> 2. 按月份统计各项测量值的平均值和标准差
> 3. 在透视表中增加一个计算字段：测量值1与测量值2的比值
>
> 请告诉我具体的操作步骤，包括每一步在哪里拖放哪个字段、选择什么汇总方式。如果是需要用计算字段的操作，请详细说明。

**预期操作指导参考**：

**分析1：合格率交叉统计**
1. 选中数据区域，插入 -> 数据透视表，放到新工作表
2. 行区域：拖入"实验人员"
3. 列区域：拖入"样品类型"
4. 值区域：拖入"是否合格"，右键 -> 值字段设置 -> 汇总方式改为"计数"
5. 再次将"是否合格"拖入值区域，右键 -> 值字段设置 -> 汇总方式改为"计数"，显示方式改为"占同行总计的百分比"（即行汇总百分比）
6. 若要精确只计算"合格"的占比，需要先对数据添加辅助列，或在值字段中筛选仅显示"合格"

**分析2：按月份统计**
1. 将"实验日期"拖入行区域，Excel 会自动按月分组
2. 如果没有自动分组，右键日期字段 -> 组合 -> 选择"月"
3. 将"测量值1"拖入值区域，汇总方式设为"平均值"
4. 再次将"测量值1"拖入值区域，汇总方式设为"标准偏差"（即标准差）
5. 对"测量值2"重复上述操作

**分析3：计算字段**
1. 在数据透视表上点击，选择"数据透视表分析" -> "字段、项目和集" -> "计算字段"
2. 名称输入"测量值比值"，公式输入 `= 测量值1 / 测量值2`
3. 点击添加 -> 确定

### 任务4：Power Query 数据清洗

**场景**：你从仪器导出的原始数据格式混乱，需要清洗后才能分析。Power Query 比手动操作更高效，且清洗步骤可重复执行。

**提示词**：

> 我从实验仪器导出了一个 CSV 文件，数据问题如下：
> - 前 5 行是仪器信息头部，不是数据，需要跳过
> - 第 6 行才是真正的表头：Time, Channel1, Channel2, Channel3, Temperature, Status
> - 数据中混有字符串 "NaN" 和 "OVERFLOW"，需要替换为 null
> - Temperature 列的值有些带单位"°C"后缀（如"25.3°C"），需要去掉单位转为数值
> - Status 列只有两种值需要保留："OK" 和 "ERROR"，其他值（如空行、"N/A"）都替换为 null
> - 最后按 Time 列升序排列
>
> 请帮我生成 Power Query 的 M 语言代码，我可以直接粘贴到高级编辑器中使用。

**预期输出参考**：

```m
let
    // 读取 CSV 文件，跳过前 5 行头部信息
    Source = Csv.Document(File.Contents("C:\Data\experiment_raw.csv"),[Delimiter=",", Columns=6, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    // 提升第 6 行作为表头（跳过前 5 行后，第 1 行就是表头）
    SkipHeader = Table.Skip(Source, 5),
    PromoteHeaders = Table.PromoteHeaders(SkipHeader, [PromoteAllScalars=true]),

    // 替换 "NaN" 和 "OVERFLOW" 为 null
    ReplaceNaN = Table.ReplaceValue(PromoteHeaders, "NaN", null, Replacer.ReplaceValue, {"Channel1", "Channel2", "Channel3", "Temperature", "Status"}),
    ReplaceOverflow = Table.ReplaceValue(ReplaceNaN, "OVERFLOW", null, Replacer.ReplaceValue, {"Channel1", "Channel2", "Channel3", "Temperature", "Status"}),

    // 清理 Temperature 列：去掉 "°C" 后缀并转为数值类型
    CleanTemperature = Table.TransformColumns(ReplaceOverflow, {{
        "Temperature",
        each if Text.Contains(Text.From(_), "°C") then
            Text.BeforeDelimiter(Text.From(_), "°C")
        else Text.From(_),
        type text
    }}),
    ChangeTempType = Table.TransformColumnTypes(CleanTemperature, {{"Temperature", type number}}),

    // 清理 Status 列：只保留 "OK" 和 "ERROR"，其他替换为 null
    CleanStatus = Table.TransformColumns(ChangeTempType, {{
        "Status",
        each if _ = "OK" or _ = "ERROR" then _ else null,
        type text
    }}),

    // 将 Channel 列转为数值类型
    ChangeTypes = Table.TransformColumnTypes(CleanStatus, {
        {"Channel1", type number},
        {"Channel2", type number},
        {"Channel3", type number}
    }),

    // 按 Time 列升序排列
    SortRows = Table.Sort(ChangeTypes, {{"Time", Order.Ascending}})
in
    SortRows
```

### 任务5：条件格式与数据可视化

**场景**：你想让数据表自动用颜色标记关键信息，一眼看出异常值和趋势。

**提示词**：

> 我的 Excel 数据表结构：
> - A列：样品编号（S001-S200）
> - B列：测量值（数值范围大约 0-100）
> - C列：偏差值（数值，可正可负）
> - D列：判定结果（Pass/Fail）
>
> 请帮我设置以下条件格式，给出具体的操作步骤或公式：
> 1. B列中，数值大于 90 的单元格填充绿色，小于 10 的填充红色
> 2. C列中，绝对值大于 5 的单元格文字加粗并标红
> 3. D列中，"Fail" 的单元格整行填充浅红色背景
> 4. A列中，样品编号按奇偶交替填充浅蓝/白色背景，方便阅读

**预期操作指导参考**：

**格式1：B列数值范围标记**
1. 选中 B2:B201
2. 开始 -> 条件格式 -> 新建规则 -> 使用公式确定要设置格式的单元格
3. 公式：`=B2>90`，格式设置为绿色填充
4. 再次新建规则，公式：`=B2<10`，格式设置为红色填充

**格式2：C列偏差超标标记**
1. 选中 C2:C201
2. 条件格式 -> 新建规则 -> 使用公式
3. 公式：`=ABS(C2)>5`
4. 格式设置：字体加粗、颜色设为红色

**格式3：Fail 行整行标记**
1. 选中 A2:D201（整行数据区域，不含表头）
2. 条件格式 -> 新建规则 -> 使用公式
3. 公式：`=$D2="Fail"`
4. 格式设置：浅红色背景填充
5. 注意 `$D2` 中的 `$` 不能省略，这确保条件判断始终基于 D 列的值

**格式4：奇偶行交替色**
1. 选中 A2:D201
2. 条件格式 -> 新建规则 -> 使用公式
3. 公式：`=MOD(ROW(),2)=0`（偶数行）
4. 格式设置：浅蓝色背景填充
5. 白色背景是默认值，无需额外设置

---

## 5. 常见问题与排错

### Q1：AI 生成的公式报 #NAME? 错误

**原因**：最常见的情况是函数名拼写错误或使用了你的 Excel 版本不支持的函数。

**解决方法**：
- 检查函数名是否正确，尤其是中文环境下的函数名（如 `AVERAGEIFS` 在中文版 Excel 中可能显示为 `AVERAGEIFS`，但部分旧函数名不同）
- 确认你的 Excel 版本：文件 -> 账户 -> 查看 Office 版本号。部分函数（如 `XLOOKUP`、`FILTER`、`UNIQUE`）仅 Office 365 或 Excel 2021 及以上版本支持
- 把报错信息和你的 Excel 版本发给 AI，让它帮你用兼容的函数重写

### Q2：VBA 宏运行时报"子过程未定义"错误

**原因**：宏代码粘贴的位置不对，或宏名称与调用时不一致。

**解决方法**：
- 确认代码粘贴在"模块"中，而不是"工作表"或"ThisWorkbook"的代码窗口中。在 VBA 编辑器左侧项目面板中，右键 -> 插入 -> 模块
- 检查 Sub 后面的宏名称是否与你运行时选择的宏名称一致
- 如果代码中引用了其他工作簿的函数，需要添加对应引用

### Q3：VBA 宏运行后数据被覆盖，无法撤销

**原因**：VBA 宏的操作无法通过 Ctrl+Z 撤销，这是 Excel 的设计限制。

**解决方法**（防患于未然）：
- 运行宏之前，先另存为工作簿副本
- 在宏代码开头添加自动备份逻辑：

```vba
' 运行前自动备份当前工作表
ThisWorkbook.SaveCopyAs ThisWorkbook.Path & "\backup_" & Format(Now, "yyyymmdd_hhmmss") & ".xlsx"
```

### Q4：Power Query 刷新后数据丢失或格式变化

**原因**：Power Query 刷新会重新执行全部步骤，如果源文件路径变了或数据格式变化，可能出问题。

**解决方法**：
- 源文件路径尽量使用相对路径或共享文件夹路径，避免因个人电脑路径不同导致问题
- 在 Power Query 的最后一步加上 `Table.Buffer()` 缓存中间结果，避免重复计算
- 如果刷新后列类型变化，检查"更改类型"步骤是否写死了列名，数据列增减时需要手动更新

### Q5：AI 生成的公式太长，难以理解和维护

**原因**：AI 有时会生成超长的嵌套公式，虽然能运行，但可读性差。

**解决方法**：
- 明确要求 AI 使用辅助列拆分逻辑。例如：让 AI 把一个复杂公式拆成 2-3 列，每列做一步中间计算
- 在提问时加上"请用辅助列方式实现，不要写超长嵌套公式"
- 对关键公式添加批注：选中单元格 -> 审阅 -> 新建批注，写明公式的用途和逻辑

### Q6：Copilot for Excel 不可用或功能有限

**原因**：Copilot 需要 Microsoft 365 Copilot 许可证，普通 Office 365 订阅不包含此功能。

**替代方案**：
- 使用对话式 AI（Claude、ChatGPT）配合手动操作，效果相当甚至更好
- 把你的 Excel 数据结构描述给 AI，让它生成公式、VBA 代码或 Power Query 步骤，你手动粘贴执行
- 对于简单操作，可以尝试在 Copilot 网页版（copilot.microsoft.com）中描述需求，虽然它不能直接操作 Excel，但可以生成操作指南

---

## 6. 进阶资源

### 本仓库示例脚本

以下文件位于 `docs/assets/examples/`，构建站点后可通过站点内链接下载。

- [excel_batch_process.bas](assets/examples/excel_batch_process.bas) — VBA 批量处理数据示例（按需修改路径与列号）

### 学习资源

- **Excel 函数速查**：微软官方文档 [support.microsoft.com](https://support.microsoft.com/zh-cn/excel) 提供所有函数的详细说明和示例
- **VBA 入门教程**：可以先让 AI 帮你生成几段 VBA 代码并逐行解释，从实践中学习比单纯看语法更高效
- **Copilot in Excel**：[support.microsoft.com/copilot-excel](https://support.microsoft.com/en-us/copilot-excel)
- **Power Query 指南**：微软 Learn 平台有系统的 Power Query 学习路径，搜索 "Power Query 学习路径" 即可找到

### 进阶技巧

- **动态数组公式**：Office 365 支持的 `FILTER`、`SORT`、`UNIQUE` 等函数可以实现以往必须用 VBA 才能做到的功能，向 AI 提问时可以注明"优先使用动态数组函数而非 VBA"
- **LAMBDA 自定义函数**：Excel 365 支持用 `LAMBDA` 创建自定义函数，适合将反复使用的公式封装成可复用的函数。可以让 AI 帮你把常用计算逻辑写成 LAMBDA 函数
- **Power Query + Power BI 联动**：如果你的数据量大或需要交互式可视化报表，可以考虑将 Power Query 清洗后的数据导入 Power BI 做可视化，AI 同样可以辅助 Power BI 的 DAX 公式编写

### 与 AI 协作的最佳实践

1. **先整理数据再提问**：确保你的数据有清晰的表头、一致的格式，AI 给出的方案会更精准
2. **小数据测试**：先用几行数据测试 AI 给出的公式或宏，确认结果正确后再应用到全量数据
3. **保存好提示词**：当你找到一个效果很好的提示词，保存下来。下次遇到类似任务时直接复用，只需要改参数
4. **逐步迭代**：如果 AI 第一次给出的方案不完美，不要从头重新提问，而是在原对话基础上追加修改要求，比如"请把公式改为忽略错误值"或"请在宏中添加进度提示"
