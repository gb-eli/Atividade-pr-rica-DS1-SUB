def menu():
    print("escolha  a fruta ")
    print("1 - Banana")
    print("2 - Abacaxi")
    print("3 - Morango")
    print("4 - Limao")
    print("5 - Manga")
    
    opcao = input("Escolha fruta: ")

    if opcao == "1":
        print("Banana!")
    elif opcao == "2":
        print("Abacaxi!")
    elif opcao == "3":
        print("Morango!")
    elif opcao == "4":
        print("Limao!")
    elif opcao == "5":
        print("Manga!")

    else:
        print("opção invalida!")

menu()
