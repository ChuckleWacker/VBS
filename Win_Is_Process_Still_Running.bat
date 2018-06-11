set i=0
set /a i+=1
start /wait "" "%commonprogramfiles%\microsoft shared\msinfo\msinfo32.exe" /categories +SWEnvRunningTasks /report "%temp%\msinforeport.txt"
>nul find /i "notepad.exe" "%temp%\msinforeport.txt"
if errorlevel 1 (
    echo program.exe not running
) else (
    echo notepad.exe still running
    pause
)