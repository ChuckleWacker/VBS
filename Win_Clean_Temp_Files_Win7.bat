::This script cleans Windows7 temporary files
:: /s = Removes specified directory including all sub-directories and files contained within
:: /q = Quiet mode

Echo Off
CD C:\Users\%Username%\AppData\Local
RMDIR /S /Q Temp