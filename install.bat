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
mkdir c:\skylan\tools\agent_logspeed
mkdir c:\skylan\tools\agent_logspeed\bin

Echo.
Echo.
Echo.

echo "Movendo os arquivos"
robocopy %origem% c:\skylan\tools\agent_logspeed\bin /e
robocopy %git% c:\skylan\tools\agent_logspeed\bin /e

Echo.
Echo.
Echo.

echo "Criando atalho no inicializar"
cd "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
del "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Agent_Logspeed"

MKlink Agente_Logspeed C:\SKYLAN\tools\agent_logspeed\bin\start.vbs

echo "links criados em: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

Echo.
Echo.
Echo.

schtasks /Create /XML C:\SKYLAN\tools\agent_logspeed\bin\task\Agent_Logspeed.xml /TN "Agent Logspeed"

set programa=agent_logspeed.exe

C:\SKYLAN\tools\agent_logspeed\bin\start.vbs

echo "Instalacao concluida."

Echo.
Echo.
Echo.

pause