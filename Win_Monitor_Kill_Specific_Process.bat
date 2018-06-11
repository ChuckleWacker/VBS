::This script monitors for a specific process, Rem out everything except what you want then run.
:: /s = Specifies the remote system to connect to
:: /u = Specifies the domain\user this should execute as
:: /p = Speicifes the password to execute with username
:: /v = Display verbose information on task/s
:: /fi = Filter for tasks: Status, ImageName, PID, Session, SessionName, CPUTime, MemUsage, Username, Services, WindowTitle, Modules
:: /fo = Save to tasklist to CSV file

::Run tasklist from a remote system
::Echo Off
::Tasklist /S [computername]

::Run tasklist under listed credentials
::Echo Off
::Tasklist /U [domain\username] /P [password]

::Run tasklist from a remote system under your credentials
::Echo Off
::Tasklist /S [comptername] /U [domain\username] /P [password]

::Run tasklist from a remote system under your credentials, filtering for a specific task
::Echo Off
::Tasklist /S [comptername] /U [domain\username] /P [password] /FI "ImageName eq [processname]"

::Kill task locally
::Echo Off
::TaskKill /F /IM "[processname]"

::Kill task from a remote system
::Echo Off
::TaskKill /S [comptername] /U [domain\username] /P [password] /F /IM "[processname]"