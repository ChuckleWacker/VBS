On Error Resume Next

Dim objExcel
Dim objWorkbookAll
Dim objWorkbookUnassigned
Dim objWorksheetAll
Dim objWorksheetUnassigned


Set objExcel = CreateObject("Excel.Application")
Set objWorkbookAll = objExcel.Workbooks.Open("ORIGINAL FILE PATH HERE.csv")
Set objWorksheetAll = objWorkbookAll.Worksheets("WORKSHEET NAME HERE")

objExcel.Visible = False

objExcel.DisplayAlerts = False

objWorkbookAll.SaveAs "SAVE AS FILE PATH & NAME HERE.xlsx", 51

objWorkbookAll.Close

objExcel.Quit


Set objExcel = Nothing
Set objWorkbookAll = Nothing
Set objWorksheetAll = Nothing
Set objWorkbookUnassigned = Nothing
Set objWorksheetUnassigned = Nothing