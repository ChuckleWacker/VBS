'On Error Resume Next

Dim objAccess

Set objAccess = createObject("Access.Application") 

objAccess.OpenCurrentDatabase("ACCESS DATABASE PATH HERE")

objAccess.docmd.runmacro "RUN (MACRO) NAME HERE"

objAccess.CloseCurrentDatabase

objAccess.Quit

Set objAccess = Nothing