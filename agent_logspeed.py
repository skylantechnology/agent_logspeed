# pyinstaller --onefile --icon=skyico_azul_claro.ico
#py -m pip install schedule
# importando bibliotecas
import schedule
import requests
import subprocess
import time
import json
import sys

#declarando varivaris
url = 'http://52.168.129.21/logs'
headers = {'content-type': 'application/json', 'X-User-Email': 'skylan@skylan.com.br','X-User-Token': 'hdBasF492V1bepbde3YP'}
rotas = []

#Metodo faz a leitura do arquivo de configuração
def ler_config():
    with open('C:\\skylan\\tools\\agent_logspeed\\bin\\config.json', 'r', encoding='utf8') as json_file:
        return json.load(json_file)


#Metodo que organiza dos dados e monta do JSON
def dados_for_post(ops,serv):
    # Execute o speed test e decodifica o retorno para o formato JSON do python
    try:
        log = subprocess.check_output('speedtest -u Mbps -s %d -f json  jsonl' % (serv), universal_newlines=True)
    except Exception as log:
        return ("Erro de requisicao", log)

    log = json.JSONDecoder().decode(log)
    cliente = subprocess.Popen("echo %USERDOMAIN%", shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
        "utf-8").strip()
    hostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
        "utf-8").strip()

    try:
        loss = log['packetLoss']
    except KeyError:
        loss = 0

    output = {
        'cli': cliente,
        'host': hostname,
        'operadora': ops,
        'isp': log['isp'],
        'timestamp': log['timestamp'],
        'p_jitter': log['ping']['jitter'],
        'p_latency': log['ping']['latency'],
        'd_bandwidth': log['download']['bandwidth'],
        'd_bytes': log['download']['bytes'],
        'd_elapsed': log['download']['elapsed'],
        'u_bandwidth': log['upload']['bandwidth'],
        'u_bytes': log['upload']['bytes'],
        'u_elapsed': log['upload']['elapsed'],
        'packetLoss': loss,
        'iface_InternalIp': log['interface']['internalIp'],
        'iface_mac': log['interface']['macAddr'],
        'iface_externalIp': log['interface']['externalIp'],
        'serv_id': log['server']['id'],
        'serv_name': log['server']['name'],
        'serv_location': log['server']['location'],
        'serv_country': log['server']['country'],
        'serv_host': log['server']['host'],
        'serv_port': log['server']['port'],
        'serv_ip': log['server']['ip']
    }
    output = json.dumps(output)
    return output

#Metodo que envia os dados para o servidor via POST
def request_dados(rotas,url,headers):
    i = 0
    limit = len(rotas)
    while i < limit:
        op = rotas[i][0]
        serv = rotas[i][1]

        #chama o metodo que retorna o JSON formatado
        output = dados_for_post(op, serv)

        ret = ""
        try:
            req = requests.post(url, data=output, headers=headers)
            ret = req.text
            print (ret)
        except Exception as ret:
            print ("Erro de requisicao", ret)

        i += 1



#chama o metodo ler_config
config = ler_config()

#organiza os dados do arquivo de configuração
for key, val in config['operadoras'].items():
    key = int(key)
    for key2, val2 in config['servidores'].items():
        key2 = int(key2)
        if key == key2:
            op = (val,val2)
            rotas.append(op)

if  config["test_time"] != " ":
    test_time = config["test_time"]
else:
    test_time = 60

if  config["check_time"] != " ":
    check_time = config["check_time"]
else:
    check_time = 1


#chama o metodo request_dados ao iniciar a aplicação
one_post = request_dados(rotas,url,headers)

#chama o metodo request_dados com base no schelule configurado
result = schedule.every(test_time).minutes.do(request_dados,rotas,url,headers)

#cria o loop do check_time conforme o tempo definido nas configurações
while True:
    schedule.run_pending()
    time.sleep(check_time)
