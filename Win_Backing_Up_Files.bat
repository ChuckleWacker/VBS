::This script backs up files from C:\Test to C:\Backup
:: /d:m-d-y = Copies files changed on or after the specified date. No date overwrites with newest file.
:: /p = Prmpts yo ubefore creating each destination file
:: /s = Copies directories and subdirectories except empty ones
:: /e = Copies directories and subdirectories including empty ones
:: /v = Verifies the size of each new file
:: /w = Prompts you to press a key before copying
:: /c = Continues copying even if errors occur
:: /i = If destination does not exist and copying more than one file, assume destination is a directory
:: /q = Does not display file names while copying
:: /f = Displays full source and ddestination file names while copying
:: /l = Displays file names that would be copied
:: /g = Allow copying of encrypted files to location that does not allow encryptiong
:: /h = Copies hidden and system files
:: /r = Overwrites read-only files
:: /t = Create directory structure but does not copy files
:: /u = Copies only files that already exist
:: /y = Suppress prompting to confirm you want to overwrite an existing destination file
:: -/y = Prompts you to confirm you want to overwrite an existing destination file
:: /z = Copies networked files in restartable mode
:: /j = Copies using unbuffered I/O. Recommended for very large files.

::Backup files to from the "C:\Test" folder to the "C:\Backup" folder. Includes subdirectories, hidden files, and overwrites with newest file version
Echo Off
XCOPY C:\Test C:\Backup /e /h /d