import openpyxl
from estrutura_API_ZABBIX import *
import json
import requests
import pandas as pd

class Le_Tabela():
    def __init__(self, tabela):
        doc_planilha = openpyxl.load_workbook(tabela)
        self.planilha = doc_planilha['Hosts']

        self.host = []
        self.visible_name = []
        self.grupos = []
        self.interfaces_tipo = []
        self.interfaces_ip = []
        self.interfaces_porta = []
        self.descricao = []
        self.templates = []

        self.le_tabela()


    def le_tabela(self):
        self.dados_hosts =[]
        for num_linha in range(4, self.planilha.max_row + 1):
            validacao_linha = True
            for celula in range(2, self.planilha.max_column + 1):
                verificacao_celula = self.verifica_celula(num_linha, celula)
                if not verificacao_celula:
                    validacao_linha = False
                    break
                else:
                    validacao_linha = True
            if validacao_linha == True:
                self.dados_hosts.append(self.le_linha2(num_linha))


    def le_linha(self, num_linha):
        dados_host = []
        self.host.append(self.planilha.cell(num_linha, 2).value)
        self.visible_name.append(self.planilha.cell(num_linha, 3).value)
        self.grupos.append((self.planilha.cell(num_linha, 4).value).split(','))
        self.interfaces_tipo.append((self.planilha.cell(num_linha, 5).value).split(','))
        self.interfaces_ip.append((self.planilha.cell(num_linha, 6).value).split(','))
        self.interfaces_porta.append(str((self.planilha.cell(num_linha, 7).value)).split(','))
        self.descricao.append(self.planilha.cell(num_linha, 8).value)
        self.templates.append((self.planilha.cell(num_linha, 9).value).split(','))
        dados_host = [self.host]

    def le_linha2(self, num_linha):
        host = self.planilha.cell(num_linha, 2).value
        visible_name = self.planilha.cell(num_linha, 3).value
        grupos = (self.planilha.cell(num_linha, 4).value).split(',')
        interfaces_tipo = (self.planilha.cell(num_linha, 5).value).split(',')
        interfaces_ip = (self.planilha.cell(num_linha, 6).value).split(',')
        interfaces_porta = str((self.planilha.cell(num_linha, 7).value)).split(',')
        descricao = self.planilha.cell(num_linha, 8).value
        templates = (self.planilha.cell(num_linha, 9).value).split(',')
        dados_host = [host, visible_name, grupos, interfaces_tipo, interfaces_ip, interfaces_porta, descricao, templates]
        return dados_host

    def verifica_celula(self, numero_linha, numero_coluna):
        valor_celula = self.planilha.cell(numero_linha, numero_coluna).value
        if not valor_celula:
            print('Verifique a linha {} célula {}'.format(numero_linha, numero_coluna))
            return None
        else:
            return valor_celula

    def filtra_grupos(self):
        for grupo_host in self.grupos:
            fatias_grupos = grupo_host.split(',')
            print(fatias_grupos)



class Zabbix():
    header = {'content-type': 'application/json'}

    def __init__(self, usuario, senha, endereco_url):
        self.url = endereco_url
        autenticacao["params"]["user"] = usuario
        autenticacao["params"]["password"] = senha

        resposta_zbx = self.envia_comando_json(autenticacao)

        if "error" in resposta_zbx:
            result = resposta_zbx["error"]["data"]
            print(result)
            print("Verifique url, header, user ou password !!!")
            print("Código sendo finalizado")
            exit()
        else:
            self.token = resposta_zbx["result"]
            # result = "Token gerado com sucesso"

    def envia_comando_json(self, comando):
        res = requests.post(self.url, data=json.dumps(comando), headers=self.header)
        resposta = json.dumps(res.json(), indent=4, sort_keys=True)
        resultado = json.loads(resposta)
        return resultado

    def consulta_id_grupo_hosts(self, nome_Grupo):
        consultas["hostgroup"]["params"]["filter"]["name"] = nome_Grupo
        consultas["hostgroup"]["auth"] = self.token
        resposta_zbx = self.envia_comando_json(consultas["hostgroup"])
        if not resposta_zbx['result']:
            result = None
        else:
            result = resposta_zbx['result'][0]['groupid']
        return result

    def cria_grupo(self, nome_grupo):
        id_grupo = self.consulta_id_grupo_hosts(nome_grupo)
        if id_grupo == None:
            criacao["hostgroup"]["params"]["name"] = nome_grupo
            criacao["hostgroup"]["auth"] = self.token
            resposta_zbx = self.envia_comando_json(criacao["hostgroup"])
            if "error" in resposta_zbx:
                print('Erro cria Host Group', nome_grupo)
                result = resposta_zbx['error']['data']
            else:
                result = resposta_zbx['result']['groupids'][0]
            return result
        return id_grupo