def menu():
    print("Escolha o sabor da pizza:")
    print("1 - Calabresa")
    print("2 - Frango com Catupiry")
    print("3 - Portuguesa")
    print("4 - Margherita")
    print("5 - Sair")

    pedido = input("Informe o nº da opção desejada: ")

    if pedido == "1":
        print("Você escolheu Calabresa 🍕")
    
    elif pedido == "2":
        print("Você escolheu Frango com Catupiry 🍕")
    
    elif pedido == "3":
        print("Você escolheu Portuguesa 🍕")
    
    elif pedido == "4":
        print("Você escolheu Margherita 🍕")
    
    elif pedido == "5":
        print("Encerrando o pedido...")
    
    else:
        print("Opção inválida!")

menu()
