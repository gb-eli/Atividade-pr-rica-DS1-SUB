def menu():
    hamburguer = 0
    batata = 0

    while True:
        print("\n1 - Comprar")
        print("2 - Ver carrinho")
        print("3 - Sair")

        op = input("Escolha: ")

        if op == "1":
            print("\n1 - Hamburguer\n2 - Batata")
            item = input("Item: ")

            if item == "1":
                hamburguer += 1
                print("Hamburguer adicionado")
            elif item == "2":
                batata += 1
                print("Batata adicionada")
            else:
                print("Opcao invalida")

        elif op == "2":
            print("\nCarrinho:")
            print("Hamburguer:", hamburguer)
            print("Batata:", batata)

        elif op == "3":
            print("Saindo")
            break

        else:
            print("Opcao invalida")

menu()