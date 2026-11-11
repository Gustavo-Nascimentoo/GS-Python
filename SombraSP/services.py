GRUPOS = ("Geral", "Idosos", "Trabalhadores de rua", "Crianças")
TIPOS_PONTO = ("Sombra", "Hidratação", "Sombra e hidratação")
FILTROS_PONTO = ("Todos", "Sombra", "Hidratação", "Sombra e hidratação")
NIVEIS = ("normal", "atenção", "perigo")


def classificar_risco(temperatura, grupo):
    limite_atencao = 30
    limite_perigo = 35
    if grupo != "Geral":
        limite_atencao = 27
        limite_perigo = 32

    if temperatura >= limite_perigo:
        return "perigo"
    elif temperatura >= limite_atencao:
        return "atenção"
    else:
        return "normal"


def gerar_recomendacao(risco):
    match risco:
        case "perigo":
            return "PERIGO: evite o sol, procure sombra ou um local fechado e beba água."
        case "atenção":
            return "ATENÇÃO: faça pausas na sombra e beba bastante água."
        case _:
            return "Normal: mantenha a hidratação."


def contar_por_risco(registros):
    contagem = {"normal": 0, "atenção": 0, "perigo": 0}
    for registro in registros:
        risco = registro["risco"]
        contagem[risco] = contagem[risco] + 1
    return contagem


def calcular_estatisticas(registros):
    if len(registros) == 0:
        return None
    temperaturas = []
    for registro in registros:
        temperaturas.append(registro["temperatura"])
    menor = min(temperaturas)
    maior = max(temperaturas)
    media = sum(temperaturas) / len(temperaturas)
    return (menor, maior, media)


def buscar_ultimo_registro(registros, bairro):
    ultimo = None
    for registro in registros:
        if registro["bairro"].lower() == bairro.lower():
            ultimo = registro
    return ultimo


def buscar_pontos_por_bairro(pontos, bairro):
    resultado = []
    for ponto in pontos:
        if ponto["bairro"].lower() == bairro.lower():
            resultado.append(ponto)
    return resultado


def filtrar_pontos(pontos, tipo):
    resultado = []
    for ponto in pontos:
        if ponto["tipo"] == tipo:
            resultado.append(ponto)
    return resultado
