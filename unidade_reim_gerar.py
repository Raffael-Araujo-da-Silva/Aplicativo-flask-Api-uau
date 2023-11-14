import requests
import json
from autent_consul import autenticar_usuario, token_entrada
import base64


#consultar unidades do cliente
#def unidade(cpf):
def unidade():
    url = 'http://187.72.213.73:3388/uauAPI/api/v1.0/Pessoas/ConsultarUnidades'
    data = json.dumps({
        "CodigoPessoa": 0,
        "CpfCnpj": "21320586104"
        #codigopessoa = tipopessoa
    })

    headers = {
        'Content-Type': 'application/json',
        'X-INTEGRATION-Authorization': token_entrada,
        'Authorization': autenticar_usuario("prouau", "123")
    }

    response = requests.request("POST", url, headers=headers, data=data)
    response_data = json.loads(response.text)

    return response_data
#recolher o numero da empresa do cliente
def empresa():
    num_empresas = [dicionario["Empresa"] for dicionario in unidade()]
    return num_empresas
empresa()

#recolher o numero da obra do cliente
def obra():
    num_obra = [dicionario["Obra"] for dicionario in unidade()]
    return num_obra
#recolher o numero da venda do cliente

def venda():
    num_venda = [dicionario["Venda"] for dicionario in unidade()]
    return num_venda

def produtos():
    num_produto = [dicionario["Produto"] for dicionario in unidade()]
    return num_produto

def reempresao():

    url = "http://187.72.213.73:3388/uauAPI/api/v1.0/BoletoServices/ConsultarBoletosReimpressao"
    num_empresa = empresa()
    num_venda = venda()
    num_obra = obra()

    data = json.dumps({
        "empresa": num_empresa[1],
        "obra": num_obra[1],
        "num_venda": num_venda[1],
        "naomostraboleto_vencido": True
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': autenticar_usuario("prouau", "123"),
        'X-INTEGRATION-Authorization': token_entrada,
    }

    response = requests.request("POST", url, headers=headers, data=data)
    response_data = response.json()
    print(response_data)
    return response_data

reempresao()


#banco do boleto
def banco_bol():
    boleto = reempresao()
    valor_boleto = boleto[0]["BoletosReimpressao"][1]["Banco_Bol"]
    print(valor_boleto)
    return valor_boleto
#numero do bolto
def SeuNum_bol():
    boleto = reempresao()
    seunumbol = boleto[0]["BoletosReimpressao"][1]["SeuNum_Bol"]
    print(seunumbol)
    return seunumbol

#gerar boleto
def gerarpdf():
    url = "http://187.72.213.73:3388/uauAPI/api/v1.0/BoletoServices/GerarPDFBoleto"

    bancobol = banco_bol()
    seunumbol = SeuNum_bol()


    data = json.dumps({
      "cod_banco": bancobol,
      "seu_numero": seunumbol,
      "ocultar_dados_pessoais": True
    })


    headers = {
      'Content-Type': 'application/json',
      'Authorization': autenticar_usuario("prouau", "123"),
      'X-INTEGRATION-Authorization': token_entrada
    }

    response = requests.request("POST", url, headers=headers, data=data)
    response_data = response.json()
    print(response_data)
    return response_data

gerarpdf()

def decodificar():
    texto_codificado = gerarpdf()
    dados_decodificados = base64.b64decode(texto_codificado)
    print(dados_decodificados)
    return dados_decodificados

decodificar()

def salvar_pdf(dados_decodificados, nome_arquivo):
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados_decodificados)

dados_decodificados = decodificar()
nome_arquivo = 'dados.pdf'

salvar_pdf(dados_decodificados, nome_arquivo)





