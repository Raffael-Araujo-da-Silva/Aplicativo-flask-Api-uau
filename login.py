from flask import Flask, render_template, request, redirect, url_for
from consul_dadosCPF import consultar_dados_pessoa
from autent_usuario import autenticar_usuario

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        senha = request.form.get('senha')

        response_data = consultar_dados_pessoa(cpf)
        primeiro_elemento = response_data[0]
        login_uau_web = {
            "retorno": primeiro_elemento
        }

        valor_loguinUauWeb = login_uau_web['retorno']['loguinUauWeb']

        token_usuario = autenticar_usuario(valor_loguinUauWeb, senha)

        if isinstance(token_usuario, str) and len(token_usuario) == 200:
            # Redirect to the home page
            return redirect('home')
        else:
            # Handle invalid credentials
            return render_template('login.html')

    return render_template('login.html')

@app.route('/home')
def home():
    # Render the home page
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)







'''def login(cpf, senha):
    response_data = consultar_dados_pessoa(cpf)
    primeiro_elemento = response_data[0]
    login_uau_web = {
        "retorno": primeiro_elemento
    }

    valor_loguinUauWeb = login_uau_web['retorno']['loguinUauWeb']

    autenticacao_sucedida = autenticar_usuario(valor_loguinUauWeb, senha)

    return autenticacao_sucedida

teste = login(70547859163, "adgar1")

if isinstance(teste, str) and len(teste) == 200:
    print("deu certo")
else:
    print("deu errado")

print(teste)'''
