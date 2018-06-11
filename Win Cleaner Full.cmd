@echo off
Set _Version=v1
Set _PC=C:
Set _PCPF=%_PC%\"Program Files"
Set _PCDS=%_PC%\"Documents and Settings"
Set _LogPC=\\PG25744\winclean
Set _WMIC=0
Set _PCName=%computername%
Set _NICSD=
Set _NICERROR=0
Set _logging=1
Set _chassis=
Set _ACTError=
Set _SAV=
Set _eTrust=
Set _chasey=1


:Start
CLS
color 07
time /t
echo.
echo Welcome to WinClean %_version%
echo.
echo This program removes temporary files and unused programs
echo. 


:INPUT
Pause


:Task1
echo.
echo Running WinClean %_version% on %_PCname%.
echo Running WinClean %_version% >> %_LogPC%\Error\t-%_pcname%.txt
Title Building User List Based On Directory.
echo Building User List Based On Directory.
echo Task 1 >> %_LogPC%\Error\t-%_pcname%.txt
:: With special thanks to Reg Mathusz.
dir /B /AD %_PCDS% > dirlist.txt
:: Determine total used disk space.
fsutil volume diskfree c: > drvspc.txt
FOR /F "tokens=8 delims= " %%d in (drvspc.txt) do Set _start=%%d
:: Create Start of event Log.
if exist %_LogPC%\log\wincleanlog.txt echo Version: %_version%, Date: %date%, Time: %time% User: %Username%, via:%_PC% On: %_PCname%>> %_LogPC%\Log\Wincleanlog.txt
SETLOCAL ENABLEEXTENSIONS
:: Store start time
FOR /f "tokens=1-4 delims=:.," %%T IN ("%TIME%") DO (
	set _starttime=%%T
	SET /a Start100S=%%T*360000+%%U*6000+%%V*100+%%W
	)
IF [%START100s%] == [] set start100s=1
echo START - Convert StartTIME:%_StartTIME%, Start 100s:%start100s% >> %_LogPC%\Error\t-%_pcname%.txt
::if exist %_bin% %_bin%\diskmon /l


:Task2
title Checking Temporary Folders.
echo Checking Temporary Folders.
::error(1): function not defined
echo Task 2 >> %_LogPC%\Error\t-%_pcname%.txt
FOR /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"%%i\local settings\temp" echo   Deleting %%i's Temporary files.
	if exist %_PCDS%\"%%i\local settings\temp" rmdir /S /Q %_PCDS%\"%%i\local settings\temp" >NUL 2>&1
	if not exist %_PCDS%\"%%i\local settings\temp" mkdir %_PCDS%\"%%i\local settings\Temp"
	)
:: Rebuild temp files that were deleted to allow applications to function normally before reboot.
if exist %_PC%\windows\temp rmdir /s /q %_PC%\windows\temp  >NUL 2>&1
if not exist %_PC%\windows\temp mkdir %_PC%\windows\temp
if exist %_PC%\winnt\temp rmdir /s /q %_PC%\winnt\temp  >NUL 2>&1
if not exist %_PC%\winnt\temp mkdir %_PC%\winnt\temp
if exist %_PC%\temp rmdir /s /q %_PC%\temp  >NUL 2>&1




:Task7
title Checking Users Cookies.
echo Checking Users Cookies.
echo task 7 Cookies >> %_LogPC%\Error\t-%_pcname%.txt
FOR /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"%%i"\cookies echo   Deleting %%i's Cookies.
	if exist %_PCDS%\"%%i"\cookies rmdir /S /Q %_PCDS%\"%%i"\cookies >NUL 2>&1
	)

:Task8
Title Deleting Prefetch Files.
echo Deleting Prefetch Files.
if exist %_PC%\%WINDIR%\Prefetch rmdir /s /q %_PC%\windows\Prefetch >NUL 2>&1
if exist %_PC%\winnt\Prefetch rmdir /s /q %_PC%\winnt\Prefetch

:Task9
title Checking Temporary Internet Folders. - This may take a while.
echo Checkinging Temporary Internet Folders.
FOR /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"%%i\Local Settings\Temporary Internet Files" echo   Deleting %%i's Temporary Internet Files.
	if exist %_PCDS%\"%%i\Local Settings\Temporary Internet Files" rmdir /S /Q %_PCDS%\"%%i\Local Settings\Temporary Internet Files" >NUL 2>&1
	)



:Task 12
title Checking for Nortel Contivity VPN client.
echo Checking for Nortel Contivity VPN client.
if exist %_PCDS%\"All Users\Desktop\Contivity VPN Client.lnk" del /f %_PCDS%\"All Users\Desktop\Contivity VPN Client.lnk"
if exist %_PCPF%\"Nortel Networks\Extranet.exe" msg * /TIME:60 /SERVER:%computername%  The Nortel Contivity VPN Client is being uninstalled.
if exist %_PCPF%\"InstallShield Installation Information\{EF964A78-078C-11D1-B7A7-0000C0134CE6}\Setup.exe" %_PCPF%\"InstallShield Installation Information\{EF964A78-078C-11D1-B7A7-0000C0134CE6}\Setup.exe" uninstall

:Task12.5
title Check for WMI controls.
echo check for WMI controls.
echo task 5 WMI >> %_LogPC%\Error\t-%_pcname%.txt
:: If WMIC is not present then skip WMI.
WMIC.EXE /? >NUL 2>&1 || GOTO task6
set _WMIC=1
echo task 12.5 _WMI=%_WMIC% >> %_LogPC%\Error\t-%_pcname%.txt
call %_logpc%\bin\"Winclean WMI.cmd"
echo task 12.5 Chassis-%_Chassis% >> %_LogPC%\Error\t-%_pcname%.txt

:Task 12.7
title Checking SMS Site name.
echo Checking SMS Site name.
if %_Site% neq RTN msg * /TIME:60 /SERVER:%computername% SCCM is not working correctly. Please install SCCM. && set _smserror=1

:Task13
title Checking for Antivirus and Old Virus Files.
echo Checking for Antivirus and Old Virus Files.
if %_logging% equ 1 echo task 13 AV >> %_LogPC%\Error\t-%_pcname%.txt
if exist %_PCPF%\"Symantec\Symantec Endpoint Protection\rtvscan.exe" goto SAV
if %_Chasey% equ 8 goto laptop
if %_Chasey% equ 9 goto laptop
if %_Chasey% equ 10 goto laptop
if %_Chasey% equ 14 goto laptop
:Desktop
if not exist %_PCPF%\"Symantec AntiVirus\Rtvscan.exe" msg * /TIME:60 /SERVER:%computername%  Symantec Antivirus is not installed. Please Install SAV. && set _SAV=1
goto SAV
:Laptop
if not exist %_PCPF%\"Symantec Client Security\Symantec AntiVirus\Rtvscan.exe" msg * /TIME:60 /SERVER:%computername%  Symantec Antivirus is not installed. Please Install SAV. && set _SAV=1
:SAV
if exist %_PC%\Windows\*.avb del /F %_PC%\Windows\*.avb
if exist %_PC%\Windows\system32\*.avb del /F %_PC%\Windows\system32\*.avb
If exist %_PC%\winnt\*.avb del /F %_PC%\winnt\*.avb
if exist %_PC%\winnt\system32\*.avb del /F %_PC%\winnt\system32\*.avb
if exist %_PCPF%\"CA\eTrust Antivirus\InocIT.exe" msg * /TIME:60 /SERVER:%computername%  eTrust is currently installed. Please Uninstall Manually. && set _eTrust=1
if exist %_PCDS%\"All Users\Start Menu\Programs\CA" rmdir /s /q %_PCDS%\"All Users\Start Menu\Programs\CA"
FOR /F "eol= tokens=1,* delims=/" %%i in (dirlist.txt) do (
	if exist %_PCDS%\"%%i\Start Menu\Programs\CA Registration" echo   Deleting %%i's eTrust Registration Files.
	if exist %_PCDS%\"%%i\Start Menu\Programs\CA Registration" rmdir /S /Q %_PCDS%\"%%i\Start Menu\Programs\CA Registration"
	)


:Task13.5
title Checking NIC speed Settings
echo Checking NIC speed Settings
echo task 13.5 NIC >> %_LogPC%\Error\t-%_pcname%.txt
 For /f "tokens=*" %%R IN ('reg query HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002bE10318} ^| Find /i "HKEY_LOCAL_MACHINE"') DO (
  For /f "tokens=3" %%N IN ('reg query %%R /v ProviderName 2^>Nul ^>Nul ^&^& reg query %%R /v ProviderName ^| More +2') DO (
    If [%%N]==[Broadcom] (
      For /f "tokens=3" %%S IN ('reg query %%R /v RequestedMediaType 2^>Nul ^>Nul ^&^& reg query %%R /v RequestedMediaType ^| More +2') DO (
        If [%%S]==[0] set _NICSD=The Broadcom NIC is hardcoded to Auto
        If [%%S]==[6] set _NICSD=The Broadcom NIC is hardcoded to 100-Full && set _NICError=1
	If [%%S]==[6] msg * /TIME:60 /SERVER:%computername%  The Broadcom NIC is hardcoded to 100-Full
        If [%%S]==[3] set _NICSD=The Broadcom NIC is hardcoded to 10-half && set _NICError=1
	If [%%S]==[3] msg * /TIME:60 /SERVER:%computername%  The Broadcom NIC is hardcoded to 10-half
      )
    )
    If [%%N]==[Intel] (
      For /f "tokens=3" %%S IN ('reg query %%R /v SpeedDuplex 2^>Nul ^>Nul ^&^& reg query %%R /v SpeedDuplex ^| More +2') DO (
        If [%%S]==[0] set _NICSD=The Intel NIC is hardcoded to Auto
        If [%%S]==[4] set _NICSD=The Intel NIC is hardcoded to 100-Full && set _NICError=1
	If [%%S]==[4] msg * /TIME:60 /SERVER:%computername% The Intel NIC is hardcoded to 100-Full
        If [%%S]==[1] set _NICSD=The Intel NIC is hardcoded to 10-half && set _NICError=1
	If [%%S]==[1] msg * /TIME:60 /SERVER:%computername% The Intel NIC is hardcoded to 100-Half
      )
    )
  )
)


:Task14
title Checking for HDD Fragmentation.
echo Checking for HDD Fragmentation.
FOR /F "tokens=2 delims= " %%i in ('defrag c: -a') DO set _Defrag=%%i
If %_Defrag% equ should msg * /TIME:60 /SERVER:%computername% The HDD needs to be Defragmented.


:Task14.5
title Checking for Absolute Computrace on Notebooks.
echo Checking for Absolute Computrace on Notebooks.
if %_chasey% equ 10 goto RPCNET
if %_chasey% equ 9 goto RPCNET
goto task15
:RPCNET
if not exist %systemroot%\system32\rpcnet.exe msg * /TIME:60 /SERVER:%computername% Computrace is NOT installed on this computer. && set _ACTError=1


:Task15
title Cleaning up.
echo Cleaning up.
echo Removing X: drive mapping.
if exist x: net use x: /delete
:: Calculate amout of drive space freed.
echo cleanup >> %_LogPC%\Error\t-%_pcname%.txt
echo Calculate amout of drive space freed. >> %_LogPC%\Error\t-%_pcname%.txt
fsutil volume diskfree c: > drvspc.txt
FOR /F "tokens=8 delims= " %%d in (drvspc.txt) do Set _end=%%d
set _endmb=%_end:~0,5%
Set _startmb=%_start:~0,5%
set /a _total=%_endmb%-%_startmb%
FSUTIL.EXE >NUL 2>&1 || set %_total%=Error

:: Retrieve Stop time.
echo Retrieve Stop time. >> %_LogPC%\Error\t-%_pcname%.txt
For /f "tokens=1-4 delims=:.," %%T IN ("%TIME%") DO (
       SET StopTIME=%TIME%
       SET /a Stop100S=%%T*360000+%%U*6000+%%V*100+%%W
       )
Set /a TookTime=%Stop100S%-%Start100S%

:: Calculating from seconds to Minutes and Seconds.
echo Calculating seconds to Minutes and Seconds. tooktime:%tooktime%, Stop:%Stop100S% start:%Start100S% >> %_LogPC%\Error\t-%_pcname%.txt
if %tooktime% GEQ 6000 (set /a _minutes=%tooktime%/6000) else set _minutes=0

echo Calculating _tookminutes Minutes:%_minutes% >> %_LogPC%\Error\t-%_pcname%.txt
set /a _tookminutes=%_minutes%*6000

echo Calculating _totaltime TookMunites:%_tookminutes% >> %_LogPC%\Error\t-%_pcname%.txt
set /a _totaltime=%tooktime%-%_tookminutes%
echo _totaltime:%_totaltime% _MFG:%_MFG% >> %_LogPC%\Error\t-%_pcname%.txt

:endlog
:: Create End Log
echo Create End Log >> %_LogPC%\Error\t-%_pcname%.txt
IF exist %_LogPC%\Log\wincleanlog.txt echo Elapsed Time: %_minutes%:%_totaltime:~0,-2%, Deleted: %_total%Mb, On: %_PCname% >> %_LogPC%\Log\wincleanlog.txt

:: Delete Directory and Drive space files.
echo Delete Directory and Drive space files. >> %_LogPC%\Error\t-%_pcname%.txt
IF exist dirlist.txt del /F dirlist.txt
IF exist drvspc.txt del /F drvspc.txt

:Display
echo display results >> %_LogPC%\Error\t-%_pcname%.txt
cls
color 2F
Title This Computer Has Been Sucessfully WinCleaned.
echo WinClean Results:
echo.

echo     Cleanup Time: M:S %_minutes%:%_totaltime:~0,-2%
echo File Space freed: %_total%Mb
IF %_WMIC% NEQ 1 goto end
echo          PC Name: %_PCName%
echo     Manufacturer: %_MFG% 
echo    Serial Number: %_SN%
echo            Model: %_model%
IF %_MFG% EQU Hewlett-Packard echo      Part Number: %_PN%
IF %_MFG% EQU FUJITSU echo      Part Number: %_PN%
echo    Installed RAM: %_RAMsize%
Echo Operating System: %_OS% Service Pack %_SPV%
echo     Chassis Type: %_Chassis%
echo          GateWay: %_GWName%
echo     Network Card: %_NICSD%
echo   AD Description: %_ADdesc%
echo   SCCM site code: %_site%
IF %_MFG% EQU Hewlett-Packard echo         %_warranty%


:Action Items
Echo Action Items:
if [%_SAV%]==[1] echo 	Install Symantec Antivirus. && color 4e
if [%_eTrust%]==[1] echo 	Uninstall eTrust Antivirus. && color 4e
if %_RAM% LSS 1000000000 echo 	Physical RAM is Less Than 1Gb. && color 4e
if %_Defrag% equ should echo 	The Hard Drive Needs to be Defragmented. && color 4e
if /I %_pcname% neq %_RIP% echo 	The forward and Reverse DNS Record Lookup Does Not Match. && color 4e
if %_PFMin% NEQ %_PFMax% echo 	The Pagefile needs to be adjusted. && color 4e
if [%_NICError%]==[1] echo         %_NICSD% &&  color 4e
if [%_ADerror%]==[1] echo 	There is a problem with the Active Directory Description. && color 4e
if [%_ACTError%]==[1] echo         CompuTrace needs to be installed. && color 4e
if [%_smserror%]==[1] echo         SMS is not setup correctly. Please install SCCM. && color 4e

:end
if %_logging% equ 1 echo End >> %_LogPC%\Error\t-%_pcname%.txt
echo.
pause
color
