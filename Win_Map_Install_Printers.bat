::This script installs printers, top is local method for heavy customization
:: RunDLL32 PrintUI.dll,PrintUIEntry [options] [@commandfile]
:: /a[file] binary file name
:: /b[name] base printer name
:: /c[name] unc machine name if the action is on a remote machine
:: /dl delete local printer
:: /dn delete network printer connection
:: /dd delete printer driver
:: /il install printer using add printer wizard
:: /in add network printer connection
:: /k print test page to specified printer, cannot be combined with command when installing a printer
:: /n[name] printer name
:: /p display printer properties
:: /q quiet mode, do not display error messages
:: /r[port] port name
:: /u use the existing printer driver if it's already installed
:: /y set printer as the default
:: /Xg get printer settings
:: /Xs set printer settings
:: /Mw[message] show a warning message before committing the command
:: /Mq[message] show a confirmation message before committing the command


::This script connects to a network printer

Echo Off

NET USE Z: /DELETE /Y 
NET USE Z: \\[PrinterServer]\[PrinterName] /PERSISTENT:YES

