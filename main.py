from flask import Flask, render_template, request
from autent_consul import autenticar_usuario, consultar_dados_pessoa
from autent_consul import token_entrada
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = r'RAFAEL'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('/login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    cpf = request.form.get('cpf')
    senha = request.form.get('senha')

    response_data = consultar_dados_pessoa(cpf)
    primeiro_elemento = response_data[0]
    login_uau_web = {
        "retorno": primeiro_elemento
    }

    valor_loguinUauWeb = login_uau_web['retorno']['loguinUauWeb']
    token_usuario = autenticar_usuario(valor_loguinUauWeb, senha)

    def consultar_dados_entrada(cpf):
        url = "http://187.72.213.73:3388/uauAPI/api/v1.0/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus"

        data = json.dumps({
            "cpf_cnpj": cpf,
            "status": 0
        })
        headers = {
            'Content-Type': 'application/json',
            'X-INTEGRATION-Authorization': token_entrada,
            'Authorization': token_usuario
        }

        response = requests.post(url, headers=headers, data=data)

        #pegar o valor da cpf
        response_data = response.json()
        primeiro_elemento = response_data[0]
        login_uau_web = {
            "retorno": primeiro_elemento
        }

        valor_loguinUauWeb = login_uau_web['retorno']['cpfCnpj']

        return valor_loguinUauWeb


    #teste de condição para verificar se vai entrar
    if cpf == consultar_dados_entrada(cpf):
        return render_template('/home.html')
    else:
        return render_template('/login.html')

if __name__ == '__main__':
    app.run(debug=True)






