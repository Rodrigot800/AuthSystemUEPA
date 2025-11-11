import requests

def login(base_url, usuario, senha):
    """
    Envia o login e senha para o servidor Flask e retorna o token se for válido.
    """
    try:
        url = f"{base_url}/login"
        dados = {"usuario": usuario, "senha": senha}
        resposta = requests.post(url, json=dados, timeout=5)

        if resposta.status_code == 200:
            return resposta.json().get("token")
        else:
            return None
    except Exception as e:
        print(f"[ERRO] Falha na conexão com o servidor: {e}")
        return None
