::This script checks for fragmentation of harddrive and defragments
:: Defragmentation
:: /A = Performs analysis on the specified volumes
:: -b = Optmizes drive for boot (hidden function)
:: /C = Performs the operation on all volumes
:: /E = Performs the operaton on all volumes except those specified
:: /H = Run the operation at normal priority (default is low)
:: /M = Run the operation on each volume in parallel in the background
:: /T = Track an operation already in progress on the specified volume
:: /U = Print the progress of the operation on the screen
:: /V >filename.txt = Print verbose output containing the fragmentation statistics, puts in txt file
:: /X = Perform free space consolidation on the specified volumes
:: Check Disk
:: /F = Fixes errors on disk
:: /V = On FAT/FAT32: Displays the full path, On NTFS: Displays cleanup messages (if any)
:: /R = Locates bad sectors and recovers readable information (implies /F)
:: /L:(size) = NTFS Only, Changes the log file size to the specified size, else shows complete size
:: /X = Forces the volume to dismount first if necessary (implies /F)
:: /I = NTFS Only, Performs less vigorous check of index entries
:: /C = NTFS Only, Skips checking of cycles within the folder structure
:: /B = NTFS Only, Re-evaluates bad clusters on the volume (implies /R)
:: ErrorLevel 3 = Abort by User

Echo Off

ChkDsk C:
If not errorlevel 3 GoTo :Defragment
If not exist C:\windows If not exist C:\pagefile.sys GoTo :DiskCheck1
GoTo :DiskCheck2

:DiskCheck1
::Echo Y | Chkdsk C: /F /X /R
Chkdsk C: /F /X /R
GoTo :Defragment

:DiskCheck2
ChkDsk C: /F /R

:Defragment
Defrag C: -b
Defrag C: 

:End