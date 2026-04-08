def menu():
    print("Escolha o hamburguer:")
    print("1 - Costela")
    print("2 - bacon")
    print("3 - crispy")
    print("4 - smash burguer")
    print("5 - Sair")

    pedido = input("Informe o nº da opção desejada: ")

    if pedido == "1":
        print("Você escolheu Costela 🍔")
    
    elif pedido == "2":
        print("Você escolheu bacon 🍔")
    
    elif pedido == "3":
        print("Você escolheu crispy 🍔")
    
    elif pedido == "4":
        print("Você escolheu smash burguer 🍔")
    
    elif pedido == "5":
        print("Encerrando o pedido...")
    
    else:
        print("Opção inválida!")

menu()