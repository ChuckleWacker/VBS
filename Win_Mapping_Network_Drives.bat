::This script maps, remaps network drives
::[devicename | *] [\\ComputerName\ShareName[\Volume] [Password | *]]
:: /User:[Domain\UserName]
:: /Delete | [/Persistent:(YES | NO)]

Echo Off

::Removes all current network drives mapped to account, and persistence
NET USE * /DELETE /Y 

::Statically Map Drives using domain cerdentials, with drive persistence.
NET USE Z: /Persistent:YES \\[Network Drive Here] /U:[Domain Here\Username Here] [Password Here]
NET USE Y: /Persistent:YES \\[Network Drive Here] /U:[Domain Here\Username Here] [Password Here]
NET USE X: /Persistent:YES \\[Network Drive Here] /U:[Domain Here\Username Here] [Password Here]
