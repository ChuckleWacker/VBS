::This script looks into the C:\Test folder, renaming the files so a zero shows up at the front of the name

Echo Off
FOR /f "tokens=*" %%a IN ('DIR /b /a-d "C:\Test\"') DO (
Rename "C:\Test\%%a" "0%%a"
)