::This script reports what hardware is on a machine

Echo Off

::Show Remote PC Hardware, Output to CSV File
::SystemInfo /S [MachineName] /U [domain\user] /P [password] > C:\CompInfo.csv
::SystemInfo /S [MachineName] /U [domain\user] /P [password] > %ComputerName%\CompInfo.csv

::Show Local PC Hardware, Output to CSV File
SystemInfo > C:\CompInfo.CSV