from funcoes import *
import pandas as pd

teste = Le_Tabela('Tabela de Hosts.xlsx')
zabbix = Zabbix('Admin', 'zabbix', "http://192.168.220.136/api_jsonrpc.php")

print(zabbix.token)
#print(zabbix.consulta_id_hosts('ACCAZ-SWITCH111'))

zabbix.cria_host(teste)
