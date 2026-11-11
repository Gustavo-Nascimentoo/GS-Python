from datetime import datetime

import database
import services
import validacoes


def mostrar_registros(registros):
    if len(registros) == 0:
        print("Nenhum registro de temperatura ainda.")
        return
    for i in range(len(registros)):
        registro = registros[i]
        numero = i + 1
        bairro = registro["bairro"]
        data_hora = registro["data_hora"]
        temperatura = registro["temperatura"]
        grupo = registro["grupo"]
        risco = registro["risco"]
        print(f"{numero} | Bairro: {bairro} | {data_hora} | {temperatura} °C | {grupo} | Risco: {risco}")


def mostrar_pontos(pontos):
    if len(pontos) == 0:
        print("Nenhum ponto de apoio encontrado.")
        return
    for i in range(len(pontos)):
        ponto = pontos[i]
        numero = i + 1
        nome = ponto["nome"]
        tipo = ponto["tipo"]
        bairro = ponto["bairro"]
        referencia = ponto["referencia"]
        print(f"{numero} | {nome} | {tipo} | Bairro: {bairro} | {referencia}")


def registrar_temperatura(dados):
    print("\n--- Registrar temperatura ---")
    bairro = validacoes.ler_texto("Bairro: ", 2)
    temperatura = validacoes.ler_float("Temperatura em °C (-10 a 60): ", -10, 60)
    grupo = validacoes.escolher_opcao("Quem está sendo observado?", services.GRUPOS)
    risco = services.classificar_risco(temperatura, grupo)
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    registro = {
        "bairro": bairro,
        "data_hora": data_hora,
        "temperatura": temperatura,
        "grupo": grupo,
        "risco": risco
    }
    dados["registros"].append(registro)

    if database.salvar_dados(dados):
        print("\nRegistro salvo!")
    print("Risco:", risco.upper())
    print(services.gerar_recomendacao(risco))


def cadastrar_ponto(dados):
    print("\n--- Cadastrar ponto de apoio ---")
    nome = validacoes.ler_texto("Nome do local: ", 3)
    tipo = validacoes.escolher_opcao("Tipo de apoio:", services.TIPOS_PONTO)
    bairro = validacoes.ler_texto("Bairro: ", 2)
    referencia = validacoes.ler_texto("Endereço ou referência: ", 3)

    ponto = {
        "nome": nome,
        "tipo": tipo,
        "bairro": bairro,
        "referencia": referencia
    }
    dados["pontos"].append(ponto)

    if database.salvar_dados(dados):
        print("\nPonto de apoio salvo!")


def listar_registros(dados):
    print("\n--- Registros de temperatura ---")
    mostrar_registros(dados["registros"])


def listar_pontos(dados):
    print("\n--- Pontos de apoio ---")
    tipo = validacoes.escolher_opcao("Filtrar por:", services.FILTROS_PONTO)
    if tipo == "Todos":
        pontos = dados["pontos"]
    else:
        pontos = services.filtrar_pontos(dados["pontos"], tipo)
    print()
    mostrar_pontos(pontos)


def consultar_bairro(dados):
    print("\n--- Situação de um bairro ---")
    bairro = validacoes.ler_texto("Bairro: ", 2)

    ultimo = services.buscar_ultimo_registro(dados["registros"], bairro)
    if ultimo is None:
        print("\nAinda não há temperatura registrada em", bairro)
    else:
        temperatura = ultimo["temperatura"]
        data_hora = ultimo["data_hora"]
        grupo = ultimo["grupo"]
        risco = ultimo["risco"]
        print(f"\nÚltimo registro: {temperatura} °C em {data_hora} ({grupo})")
        print("Risco:", risco.upper())
        print(services.gerar_recomendacao(risco))

    print("\nPontos de apoio em", bairro + ":")
    mostrar_pontos(services.buscar_pontos_por_bairro(dados["pontos"], bairro))


def resumo_geral(dados):
    print("\n--- Resumo geral ---")
    registros = dados["registros"]
    print("Registros de temperatura:", len(registros))
    print("Pontos de apoio cadastrados:", len(dados["pontos"]))

    contagem = services.contar_por_risco(registros)
    for nivel in services.NIVEIS:
        print("Risco", nivel + ":", contagem[nivel])

    estatisticas = services.calcular_estatisticas(registros)
    if estatisticas is not None:
        menor, maior, media = estatisticas
        print("Temperatura mínima:", menor, "°C")
        print("Temperatura máxima:", maior, "°C")
        print("Temperatura média:", round(media, 1), "°C")


def remover_registro(dados):
    print("\n--- Remover registro de temperatura ---")
    if len(dados["registros"]) == 0:
        print("Não há registros para remover.")
        return
    mostrar_registros(dados["registros"])
    numero = validacoes.ler_inteiro("Número do registro a remover (0 para cancelar): ", 0, len(dados["registros"]))
    if numero == 0:
        print("Operação cancelada.")
        return
    if validacoes.confirmar("Tem certeza que quer remover o registro " + str(numero) + "?"):
        dados["registros"].pop(numero - 1)
        database.salvar_dados(dados)
        print("Registro removido.")
    else:
        print("Operação cancelada.")


def remover_ponto(dados):
    print("\n--- Remover ponto de apoio ---")
    if len(dados["pontos"]) == 0:
        print("Não há pontos de apoio para remover.")
        return
    mostrar_pontos(dados["pontos"])
    numero = validacoes.ler_inteiro("Número do ponto a remover (0 para cancelar): ", 0, len(dados["pontos"]))
    if numero == 0:
        print("Operação cancelada.")
        return
    if validacoes.confirmar("Tem certeza que quer remover o ponto " + str(numero) + "?"):
        dados["pontos"].pop(numero - 1)
        database.salvar_dados(dados)
        print("Ponto de apoio removido.")
    else:
        print("Operação cancelada.")
