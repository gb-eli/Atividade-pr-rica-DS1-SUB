def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Comprar")
    print("2 - Ver carrinho")
    print("3 - Sair")


def menu_compras():
    print("\n=== MENU DE COMPRAS ===")
    print("1 - Hamburguer (R$12)")
    print("2 - Batata (R$8)")
    print("3 - Voltar")


def menu_carrinho():
    print("\n=== CARRINHO ===")
    print("1 - Remover hamburguer")
    print("2 - Remover batata")
    print("3 - Voltar")


def ver_carrinho(hamburguer, batata, total):
    print("\n=== SEU CARRINHO ===")

    if hamburguer == 0 and batata == 0:
        print("Carrinho vazio.")
    else:
        print("Hamburguer:", hamburguer)
        print("Batata:", batata)
        print(f"Total: R$ {total:.2f}")


def main():
    total = 0
    hamburguer = 0
    batata = 0

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            while True:
                menu_compras()
                compra = input("Escolha um item: ")

                if compra == "1":
                    hamburguer += 1
                    total += 12
                    print("Hamburguer adicionado.")

                elif compra == "2":
                    batata += 1
                    total += 8
                    print("Batata adicionada.")

                elif compra == "3":
                    break

                else:
                    print("Opcao invalida.")

        elif opcao == "2":
            while True:
                ver_carrinho(hamburguer, batata, total)

                if hamburguer == 0 and batata == 0:
                    break

                menu_carrinho()
                acao = input("Escolha uma opcao: ")

                if acao == "1":
                    if hamburguer > 0:
                        hamburguer -= 1
                        total -= 12
                        print("Hamburguer removido.")
                    else:
                        print("Nenhum hamburguer para remover.")

                elif acao == "2":
                    if batata > 0:
                        batata -= 1
                        total -= 8
                        print("Batata removida.")
                    else:
                        print("Nenhuma batata para remover.")

                elif acao == "3":
                    break

                else:
                    print("Opcao invalida.")

        elif opcao == "3":
            print("Encerrando programa.")
            break

        else:
            print("Opcao invalida.")


main()