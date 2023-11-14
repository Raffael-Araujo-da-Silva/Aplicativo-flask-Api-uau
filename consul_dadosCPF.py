import requests
from autent_usuario import token_entrada, autenticar_usuario
import json
def consultar_dados_pessoa(cpf):
    url = "http://187.72.213.73:3388/uauAPI/api/v1.0/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus"

    data = json.dumps({
        "cpf_cnpj": cpf,
        "status": 0
    })
    headers = {
        'Content-Type': 'application/json',
        'X-INTEGRATION-Authorization': token_entrada,
        'Authorization': autenticar_usuario("rafaell", "ny20ct30")
    }

    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    #print(response_data)
    return response_data
