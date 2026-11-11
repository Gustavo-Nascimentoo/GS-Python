import controller
import database
import validacoes


def exibir_menu():
    print("\n" + "=" * 46)
    print("   SOMBRASP - Alerta de Calor em São Paulo")
    print("=" * 46)
    print("1 - Registrar temperatura")
    print("2 - Cadastrar ponto de apoio")
    print("3 - Listar registros de temperatura")
    print("4 - Listar pontos de apoio")
    print("5 - Consultar situação de um bairro")
    print("6 - Resumo geral")
    print("7 - Remover registro de temperatura")
    print("8 - Remover ponto de apoio")
    print("0 - Sair")
    print("-" * 46)


def main():
    dados = database.carregar_dados()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        match opcao:
            case "1":
                controller.registrar_temperatura(dados)
            case "2":
                controller.cadastrar_ponto(dados)
            case "3":
                controller.listar_registros(dados)
            case "4":
                controller.listar_pontos(dados)
            case "5":
                controller.consultar_bairro(dados)
            case "6":
                controller.resumo_geral(dados)
            case "7":
                controller.remover_registro(dados)
            case "8":
                controller.remover_ponto(dados)
            case "0":
                print("\nAté logo! Cuide-se no calor.")
                break
            case _:
                print("Opção inválida. Digite um número de 0 a 8.")
                continue

        if not validacoes.confirmar("\nDeseja mais alguma coisa?"):
            print("\nAté logo! Cuide-se no calor.")
            break


main()
