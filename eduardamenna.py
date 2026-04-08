def menu():
    print("Início")
    print("1 - Fazer login")
    print("2 - Fazer cadastro")
    print("3 - Sair")

    pedido = input("Informe o número da opção desejada:")

    if pedido == "1":
        print("Você escolheu fazer login")

    elif pedido == "2":
        print("Você escolheu fazer o cadastro")
    
    elif pedido == "3":
        print("Você escolheu sair")
    
    else:
        print("Opção inválida!")

menu()
