@echo off
set programa=agent_logspeed.exe

tasklist /FI "IMAGENAME eq agent_logspeed.exe" 2>NUL | find /I /N "agent_logspeed.exe">NUL
if "%ERRORLEVEL%"=="0" (
    	echo O %programa% esta aberto.
) else (
	echo "Reiniciando o programa"
    	C:\SKYLAN\tools\agent_logspeed\bin\agent_logspeed.exe
)
exit
