On Error Resume Next

Dim objExcel
Dim objWorkbook
Dim objWorksheet


Set objExcel = CreateObject("Excel.Application")
Set objWorkbook = objExcel.Workbooks.Open("ORIGINAL FILE PATH HERE")
Set objWorksheet = objWorkbook.Worksheets("WORKSHEET NAME HERE")

objExcel.Visible = True

objExcel.DisplayAlerts = False

objWorksheet.Rows("1:4").Delete

objWorkbook.SaveAs "SAVE FILE PATH HERE", 51

objWorkbook.Close

objExcel.Quit

Set objExcel = Nothing
Set objWorkbook = Nothing
Set objWorksheet = Nothing
