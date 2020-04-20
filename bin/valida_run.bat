@echo off
set programa=agente_logspeed.exe

tasklist /FI "IMAGENAME eq agente_logspeed.exe" 2>NUL | find /I /N "agente_logspeed.exe">NUL
if "%ERRORLEVEL%"=="0" (
    	echo O %programa% esta aberto.
) else (
	echo "Reiniciando o programa"
    	C:\SKYLAN\tools\agente_logspeed\bin\agente_logspeed.exe
)
exit
