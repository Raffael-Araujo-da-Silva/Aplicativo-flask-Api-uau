import requests
import json

token_entrada = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..1S590K8slT-QTbD6CWNoxA.RQ5NYNVwYSO5Brx5VksUQOYdHoAAIiAMZEun-ej75-oz68yQypPRsxXT4xfHh0CVyYoBbkJ-cwv4igWjYIIO_01xQ-D7yCVHbqVJ1O-C_K-0bbNGm7DUnS8nAHlQMVahjodbezNi8Vxzaw8MdFyzzT1Yyw68aAcgjU4CEdgyUX4.CJSc3ke4dwFFf_K_20EedA'


def autenticar_usuario(login, senha):
    url = "http://187.72.213.73:3388/uauAPI/api/v1.0/Autenticador/AutenticarUsuario"

    data = json.dumps({
        "Login": login,
        "UsuarioUAUSite": login,
        "Senha": senha
    })
    headers = {
        'Content-Type': 'application/json',
        'X-INTEGRATION-Authorization': token_entrada,
    }

    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    #print(response_data)
    return response_data

#print(autenticar_usuario("rafaell", "ny20ct30"))