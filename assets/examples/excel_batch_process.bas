' Excel VBA 批量处理模板
' 用途：遍历工作簿中所有工作表，执行统一的数据处理操作
' 使用：在VBA编辑器中粘贴此代码，修改处理逻辑后运行

Sub BatchProcessSheets()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long
    Dim processedCount As Integer

    processedCount = 0

    ' 遍历所有工作表
    For Each ws In ThisWorkbook.Worksheets
        ' 跳过汇总表（如果存在）
        If ws.Name <> "汇总" Then
            ' 获取最后一行
            lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row

            ' ===== 在此处添加你的处理逻辑 =====

            ' 示例：在D列添加计算结果
            ws.Cells(1, 4).Value = "计算结果"
            For i = 2 To lastRow
                ' 修改这里的计算公式
                ws.Cells(i, 4).Value = ws.Cells(i, 2).Value * ws.Cells(i, 3).Value
            Next i

            ' ==================================

            processedCount = processedCount + 1
        End If
    Next ws

    MsgBox processedCount & " 个工作表处理完成", vbInformation
End Sub

' 运行前自动备份（建议始终调用）
Sub RunWithBackup()
    ' 备份当前工作簿
    Dim backupPath As String
    backupPath = ThisWorkbook.Path & "\backup_" & _
        Format(Now, "yyyymmdd_hhmmss") & ".xlsx"
    ThisWorkbook.SaveCopyAs backupPath

    ' 运行处理
    Call BatchProcessSheets
End Sub
