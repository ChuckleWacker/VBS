@echo off
SET _Version=v1.0
SET _PC=C:
SET _PCDS=%_PC%\"Documents and Settings"
SET _PCPF=%_PC%\"Program Files"
SET _PCName=%computername%
SET _Logging=1

:: WindowsCleaner Revision History:
:: Version 1.0 - 

:Start
cls
color 07
time /t
echo.
echo Welcome to WindowsCleaner %_Version% Updated: 08/18/2011
echo Created by Daniel Boggs.
echo.
echo This program removes temporary files, folder, and caches
echo.
echo Running WindowsCleaner %_Version% on %_PCname%.
echo.
::Pause

:Task1
Title Building User List Based On Directory.
echo Building User List Based On Directory.

:: Create directory list for script to utilze.
dir /B /AD %_PCDS% > dirlist.txt
:: Determine total used disk space.
fsutil volume diskfree c: > drvspc.txt
for /F "tokens=8 delims= " %%d in (drvspc.txt) do SET _start=%%d
SETLocal ENABLEEXTENSIONS
:: Store start time.
for /f "tokens=1-4 delims=:.," %%T in ("%Time%") do (
	SET _starttime=%%T
	SET /a Start100S=%%T*360000+%%U*6000+%%V*100+%%W
	)
if [%Start100s%] == [] SET start100s=1

:Task2
Title Checking Prefetch Files.
echo Checking\Cleaning Prefetch Files.
if exist %_PC%\%WINDIR%\Prefetch rmdir /s /q %_PC%\WINDOWS\Prefetch >nul 2>&1

:Task3
Title Checking Users Cookies.
echo Checking\Cleaning Users Cookies.
for /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"%%i"\Cookies echo   Deleting %%i's Cookies.
	if exist %_PCDS%\"%%i"\Cookies rmdir /S /Q %_PCDS%\"%%i"\Cookies >nul 2>&1
	if exist %_PCDS%\"%%i"\Application Data\Microsoft\Internet Explorer\UserData rmdir /S /Q %_PCDS%\"%%i"\Application Data\Microsoft\Internet Explorer\UserData >nul 2>&1
	)

:Task4
Title Checking Temporary Folders.
echo Checking\Cleaning Temporary Folders.
for /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"%%i\local settings\temp" echo   Deleting %%i's Temporary Files.
	if exist %_PCDS%\"%%i\local settings\temp" rmdir /S /Q %_PCDS%\"%%i\local settings\temp" >nul 2>&1
	::REM'd out for persistent pushes, only use for manual cleaning
	::if exist C:\WINDOWS\Temp rmdir /S /Q C:\WINDOWS\Temp >nul 2>&1
	if not exist C:\WINDOWS\Temp\*.qsp rmdir /S /Q C:\WINDOWS\Temp >nul 2>&1
	if not exist %_PCDS%\"%%i\local settings\temp" mkdir %_PCDS%\"%%i\local settings\temp"
	if not exist C:\WINDOWS\Temp mkdir C:\WINDOWS\Temp
	)
:: Rebuild temp files that were deleted to allow applications to function normally before reboot.
::if exist %_PC%\windows\temp rmdir /s /q %_PC%\windows\temp  >nul 2>&1
::if not exist %_PC%\windows\temp mkdir %_PC%\windows\temp
::if exist %_PC%\temp rmdir /s /q %_PC%\temp  >nul 2>&1

:Task5
Title Checking Temporary Internet Folders.
echo Checking\Cleaning Temporary Internet Folders.
for /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"%%i\Local Settings\Temporary Internet Files" echo   Deleting %%i's Temporary Internet Files.
	if exist %_PCDS%\"%%i\Local Settings\Temporary Internet Files" rmdir /S /Q %_PCDS%\"%%i\Local Settings\Temporary Internet Files" >nul 2>&1
	)

:Task6
Title Checking Symantec LiveUpdate Cache
echo Checking\Cleaning Symantec LiveUpdate Cache
for /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"All Users\Application Data\Symantec\LiveUpdate\Downloads" echo   Deleting Symantec LiveUpdate Cache.
	if exist %_PCDS%\"All Users\Application Data\Symantec\LiveUpdate\Downloads" rmdir /S /Q %_PCDS%\"All Users\Application Data\Symantec\LiveUpdate\Downloads" >nul 2>&1
	)

:Task7
Title Calculating Spaced Cleared.
fsutil volume diskfree c: > drvspc.txt
for /F "tokens=8 delims= " %%d in (drvspc.txt) do Set _end=%%d
SET _endmb=%_end:~0,5%
SET _startmb=%_start:~0,5%
SET /a _total=%_endmb%-%_startmb%
fsutil.exe >nul 2>&1 || SET %_total%=Error
echo
echo
echo Cleaned: %_total%Mb

:End
del dirlist.txt
del drvspc.txt
echo.
Pause
color
