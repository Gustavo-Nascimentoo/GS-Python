import json

ARQUIVO = "dados.json"


def carregar_dados():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return {"registros": [], "pontos": []}
    except json.JSONDecodeError:
        print("O arquivo dados.json está com problema. Começando com dados vazios.")
        return {"registros": [], "pontos": []}

    if "registros" not in dados or "pontos" not in dados:
        print("O arquivo dados.json está no formato errado. Começando com dados vazios.")
        return {"registros": [], "pontos": []}
    return dados


def salvar_dados(dados):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        return True
    except Exception as erro:
        print("Erro ao salvar o arquivo dados.json:", erro)
        return False
