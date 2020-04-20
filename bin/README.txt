Pré-requisito
	python 3 ~ >


Instalação:

PASSO 1:
	Baixe o pacote do agente-logspeed


PASSO 2:
	Mova o pacote para o diretório c:\slylan\tools


PASSO 3:

	Opção1 - agente_logspeed_no_loop.exe
	
		Crie um tarefa no agendador de tarefas do windows
		Defina o tempo de execução, por padrão vamos trabalhar com 60 minutos
		Em ações, procure o EXE no caminho a baixo
			c:\slylan\tools\agente_logspeed_no_loop.exe
			
		OBS: caso o equipamento esteja conectado a um domínio, crie um usuário de serviço para essa tarefa.

	Opção2 - Opção2 - agente_logspeed.exe

		Essa versão utiliza o schedule do python, portando bata colocar o executável para iniciar junto com o computador, 
		se fizer isso pelo Agendador de tarefas, o agente_logspeed vai rodar em segundo plano.
		
		O Schedule vai ficar verificando a cada 5 minutos se existe uma JOB a ser enviada.
		A Job está por padrão será enviada a cada 60 minutos
		
		Caso queria personalizar esses valores, siga as orientações a baixo

		Alterar o tempo de verificação do schedule
			 agente_logspeed.exe -s [tempo em segundos]

		Alterar o intervalo de execução da job
			agente_logspeed.exe -t [tempo em minutos]

		Alterar ambos os valores na mesma chamada
			agente_logspeed.exe -s [tempo em segundos] -t [tempo em minutos]