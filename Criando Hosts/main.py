from funcoes import *
import pandas as pd

teste = Le_Tabela('Tabela de Hosts.xlsx')
zabbix = Zabbix('Admin', 'zabbix', "http://192.168.220.136/api_jsonrpc.php")

print(pd.DataFrame(teste.dados_hosts))
