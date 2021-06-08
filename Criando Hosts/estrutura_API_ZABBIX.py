autenticacao = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "teste",
            "password": "teste"
        },
        'auth': None,
        "id": 1
}
consultas = {
    "hostgroup": {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": "groupid",
            "filter": {
                "name": ["teste"]
            }
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "hostname": {
 	    "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["host"],
            "filter": {
                "name": ["'$NOME_HOST'"]
            }
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "itemId": {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": ["itemid"],
            "hostids": ["'$HOST_ID'"],
            "filter": {
                "name": ["'$NOME_ITEM'"]
            }
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "hostinterface": {
        "jsonrpc": "2.0",
        "method": "hostinterface.get",
        "params": {
            "output": ["ip"],
            "hostids": "'$ID_HOST'"
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "hostid": {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid"],
            "filter": {
                "name": ["'$NOME_HOST'"]
            }
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    'hosts': {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["name"]
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "mapa":{
        "jsonrpc": "2.0",
        "method": "map.get",
        "params": {
            "output": "extend",
            "selectSelements": "extend",
            "selectLinks": "extend",
            "selectUsers": "extend",
            "selectUserGroups": "extend",
            "selectShapes": "extend",
            "selectLines": "extend",
            "filter": {
                "name": '$NOMEMAPA'
            }
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "imagem": {
        "jsonrpc": "2.0",
        "method": "image.get",
        "params": {
            "output": "imageid",
            "filter": {
                "name": "'$NOMEIMAGEM'"
            }
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "imagens": {
        "jsonrpc": "2.0",
        "method": "image.get",
        "params": {
            "output": "imageid"
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    'trigger': {
        "jsonrpc": "2.0",
        "method": "trigger.get",
        "params": {
            "itemids": '$IDItem',
            "output": ["triggerid", "expression"]
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    'script': {
        "jsonrpc": "2.0",
        "method": "script.get",
        "params": {
            "output": ["scriptid"]
        },
        "auth": "038e1d7b1735c6a5436ee9eae095879e",
        "id": 1
    },
    'id_mapa': {
        "jsonrpc": "2.0",
        "method": "map.get",
        "params": {
            "output": ['sysmapid'],
            'filter': {
                'name': []
            }
        },
        "auth": "038e1d7b1735c6a5436ee9eae095879e",
        "id": 1
    },
    'proxy': {
        "jsonrpc": "2.0",
        "method": "proxy.get",
        "params": {
            "output": "proxyid",
            "filter": {
                "host": "Teste"
            }
        },
        "auth": "038e1d7b1735c6a5436ee9eae095879e",
        "id": 1
    }
}
criacao={
    "hostgroup": {
        "jsonrpc": "2.0",
        "method": "hostgroup.create",
        "params": {
            "name": "'$NOMEGRUPOHOST'"
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "host": {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": "'$HOSTNAME'",
            "name": "'$VISIBLENAME'",
            "interfaces": [],
            'proxy_hostid': '',
            "groups": ""
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "item": {
        'system_run':{
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
                "name": "'$NOME_ITEM'",
                "key_":"'$KEY'",
                "hostid":"'$ID_HOST'",
                "interfaceid":"'$INTERFACE_ID'",
                "type":0,
                "value_type":4,
                "delay":"1",
                "history":"60d"
            },
        "auth":"'$TOKEN'",
        "id":1
        },
        'item_master': {
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
                "name": "'$ITEM_MASTER_NAME'",
                "key_":"vfs.file.contents[/tmp/arkhe_status/'$ITEM_MASTER_NAME']",
                "hostid":"'$ID_HOST'",
                "interfaceid":"'$INTERFACE_ID'",
                "type":0,
                "value_type":4,
                "delay":"5",
                "history":"60d"
            },
            "auth":"'$TOKEN'",
            "id":1
        },
        'item_dependente': {
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
                "type":18,
                "name": "'$NOMEITEM'",
                "key_": "'$ITEM_MASTER_NAME'.'$NOMEITEM'",
                "hostid":"'$ID_HOST'",
                "value_type":3,
                "master_itemid":"'$IDITEMMASTER'",
                "preprocessing":[
                    {
                        "type":5,
                        "params": '$CHAVE'
                    }
                ]
            },
            "auth":"'$TOKEN'",
            "id":1
        }
    },
    "trigger": {
        "jsonrpc": "2.0",
        "method": "trigger.create",
        "params": [],
        "auth": "'$TOKEN'",
        "id": 1
    },
    "script": {
        "jsonrpc": "2.0",
        "method": "script.create",
        "params": {
            "name": '$NOME_SCRIPT',
            "command": '$COMANDO',
            "host_access": 3,
            "execute_on": 0,
            "confirmation": "'$MENSAGEM_CONFIMACAO'",
            "groupid": '$ID_GRUPO_HOST'
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "imagem": {
        "jsonrpc": "2.0",
        "method": "image.create",
        "params": {
            "imagetype": 1,
            "name": None,
            "image": None
        },
        "auth": "'$TOKEN'",
        "id": 1
    },
    "mapa": {
        "jsonrpc": "2.0",
        "method": "map.create",
        "params": {

        },
        "auth": "'$TOKEN'",
        "id": 1

    }
}
deleta = {
    "imagem": {
        "jsonrpc": "2.0",
        "method": "image.delete",
        "params": None,
        "auth": "3a57200802b24cda67c4e4010b50c065",
        "id": 1
    },
    'host': {
        "jsonrpc": "2.0",
        "method": "host.delete",
        "params": [],
        "auth": "038e1d7b1735c6a5436ee9eae095879e",
        "id": 1
    },
    'script': {
        "jsonrpc": "2.0",
        "method": "script.delete",
        "params": [],
        "auth": "3a57200802b24cda67c4e4010b50c065",
        "id": 1
    },
    'mapa':{
        "jsonrpc": "2.0",
        "method": "map.delete",
        "params": [],
        "auth": "3a57200802b24cda67c4e4010b50c065",
        "id": 1
    }
}
elementos_mapa = {
    "imagem": {
        "elementtype": 4,
        "iconid_off": None,
        "iconid_on": "0",
        "label": "Newelement",
        "label_location": "-1",
        "x": "$CORDENADA_X",
        "y": "$CORDENADA_Y",
        "iconid_disabled": "0",
        "iconid_maintenance": "0",
        "elementsubtype": "0",
        "areatype": "0",
        "width": "200",
        "height": "200",
        "viewtype": "0",
        "use_iconmap": "0",
        "application": "",
        "elements": [],
        "urls": [],
        "permission": 2
    },
    'trigger': {
        "elementid": "$IDTRIGGER_UNITARIA",
        "iconid_on": "$IDIMAGEM",
        "label": "",
        "label_location": 2,
        "x": "$CORDENADA_X",
        "y": "$CORDENADA_Y",
        "elementtype": 2,
        "iconid_off": "$IDIMAGEMDEFAULT"
    },
    'botao': {
        "elementtype": 0,
        "iconid_off": "$IDIMAGEM",
        "iconid_on": "$IDIMAGEM",
        "x": "$CORDENADA_X",
        "y": "$CORDENADA_Y",
        "elements": [{"hostid": "$IDHOST"}]
    }
}

interface_dict = {
    "type": 1,
    "main": 1,
    "useip": 1,
    "ip": "'$IPHOST'",
    "dns": "",
    "port": "10050"
}