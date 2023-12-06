import requests
import json
import sys
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

#config = dotenv_values(".env")
#print(os.getenv("API_DOMAIN"))
#print(os.getenv("API_TOKEN"))
#print(config["API_DOMAIN"])

# obtem dados relativos a uma op especifica
def getop(op_id):
    try:
        api_url = os.getenv("API_DOMAIN")+"api.search"
        req = {"id": op_id}
        headers = {"content-Type": "application/json", "Authorization": os.getenv("API_TOKEN")}
        resp = requests.post(api_url, data=json.dumps(req), headers=headers)
        if (resp.status_code == 200):
            data = json.loads(resp.content)
            return data
        else:
            return {
                "success": False,
                "Erro": resp.status_code
            }    

    except resp.exceptions.HTTPError as error:
        return {
            "success": False,
            "Erro": error
        }

        
# registra a peça no ERP    
def setRoll(roll_data):
    try:
        api_url = os.getenv("API_DOMAIN")+"api_peca"
        req = {
            "op_id": roll_data["op_id"],
            "peca": roll_data["numero"],
            "artigo": roll_data["codprod"],
            "sequencial": roll_data["sequencial"],
            "tecelao_id": roll_data["tecelao"], 
            "tara": roll_data["tara"],
            "peso": roll_data["pB"],
            "defeitos": roll_data["defeitos"],
            "comentarios": roll_data["comentarios"],
            "posicao": roll_data["posicao"]
        }
        headers = {
            "content-Type": "application/json",
            "Authorization": os.getenv("API_TOKEN")
        }
        resp = requests.post(api_url, data=json.dumps(req), headers=headers)
        if (resp.status_code == 200):
            data = json.loads(resp.content)
            return data
        else:
            return {
                "success": False,
                "Erro": resp.status_code
            }    
    except resp.exceptions.HTTPError as error:
        return {
            "success": False,
            "Erro": error
        }

                    
# resgata todas as ops pendentes de encerramento
def getAllOps():
    try:
        api_url = os.getenv("API_DOMAIN")+"api_allop"
        headers = {
            "content-Type": "application/json",
            "Authorization": os.getenv("API_TOKEN")
        }
        resp = requests.get(api_url, data="", headers=headers)
        if (resp.status_code == 200):
            data = json.loads(resp.content)
            return data
        else:
            return {
                "success": False,
                "Erro": resp.status_code
            }    
    except resp.exceptions.HTTPError as error:
        return {
            "success": False,
            "Erro": error
        }


# resgata os dados dos teceloes
def getTeceloes():
    try:
        api_url = os.getenv("API_DOMAIN")+"api_teceloes"
        headers = {
            "content-Type": "application/json",
            "Authorization": os.getenv("API_TOKEN")
        }
        resp = requests.get(api_url, data="", headers=headers)
        if (resp.status_code == 200):
            data = json.loads(resp.content)
            return data
        else:
            return {
                "success": False,
                "Erro": resp.status_code
            }    
    except resp.exceptions.HTTPError as error:
        return {
            "success": False,
            "Erro": error
        }