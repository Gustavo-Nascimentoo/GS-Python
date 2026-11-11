def ler_texto(mensagem, minimo):
    while True:
        texto = input(mensagem).strip()
        if len(texto) >= minimo:
            return texto
        print("Entrada inválida: digite pelo menos", minimo, "caracteres.")


def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            numero = int(input(mensagem))
        except ValueError:
            print("Entrada inválida: digite um número inteiro.")
            continue
        if numero >= minimo and numero <= maximo:
            return numero
        print("Valor fora do intervalo: digite de", minimo, "a", maximo)


def ler_float(mensagem, minimo, maximo):
    while True:
        try:
            numero = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida: digite um número (ex.: 32.5 ou 32,5).")
            continue
        if numero >= minimo and numero <= maximo:
            return numero
        print("Valor fora do intervalo: digite de", minimo, "a", maximo)


def escolher_opcao(titulo, opcoes):
    print(titulo)
    for i in range(len(opcoes)):
        print(i + 1, "-", opcoes[i])
    escolha = ler_inteiro("Número da opção: ", 1, len(opcoes))
    return opcoes[escolha - 1]


def confirmar(mensagem):
    while True:
        resposta = input(mensagem + " (s/n): ").strip().lower()
        if resposta == "s" or resposta == "sim":
            return True
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            return False
        else:
            print("Responda com 's' ou 'n'.")
