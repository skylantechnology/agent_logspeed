@echo off

Echo.
Echo.
Echo.

SET origem="%~dp0bin"

cd  %origem%

Echo.
Echo.
Echo.

echo "Criando diretorio de destino"
mkdir c:\skylan\tools
mkdir c:\skylan\tools\agente_logspeed
mkdir c:\skylan\tools\agente_logspeed\bin

Echo.
Echo.
Echo.

echo "Movendo os arquivos"
robocopy %origem% c:\skylan\tools\agente_logspeed\bin /e
robocopy %git% c:\skylan\tools\agente_logspeed\bin /e

Echo.
Echo.
Echo.

echo "Criando atalho no inicializar"
cd "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
del "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Agente_Logspeed"

MKlink Agente_Logspeed C:\SKYLAN\tools\agente_logspeed\bin\start.vbs

echo "links criados em: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

Echo.
Echo.
Echo.

schtasks /Create /XML C:\SKYLAN\tools\agente_logspeed\bin\task\Agente_Logspeed.xml /TN "Agente Logspeed"

set programa=agente_logspeed.exe

C:\SKYLAN\tools\agente_logspeed\bin\start.vbs

echo "Instalacao concluida."

Echo.
Echo.
Echo.

pause
