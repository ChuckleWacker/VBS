On Error Resume Next
Do
  Set xl = GetObject(, "Excel.Application")
  status = Err.Number
  If status = 0 Then
    For Each wb in xl.Workbooks
      wb.Close False  'discard changes in open workbooks
    Next
    xl.Quit
  ElseIf status <> 429 Then
    WScript.Echo Err.Number & ": " & Err.Description
    WScript.Quit 1
  End If
Until status = 429
On Error Goto 0