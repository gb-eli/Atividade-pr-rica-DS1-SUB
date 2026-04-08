def xiomi():
    print(" Escolha seu celular Xiomi: ")
    print("Qual você deseja comprar? ")
    print("1. Xiomi Redmi Note 11 Pro")
    print("2. Xiomi Redmi Note 12 Pro Plus")
    print("3. Xiomi Redmi Note 15 Pro Max")
    print("4. Xiomi Redmi Note 14 Pro Ultra")
    print("5. Sair")

def iphone():
    print(" Escolha seu celular Iphone: ")
    print("Qual você deseja comprar? ")
    print("1. Iphone 15 Pro Max")
    print("2. Iphone 15 Pro")
    print("3. Iphone X")
    print("4. Iphone 11")
    print("5. Sair")

def samsung():
    print(" Escolha seu celular Samsung: ")
    print("Qual você deseja comprar? ")
    print("2. Samsung Galaxy S24 Ultra")
    print("3. S26 Plus")
    print("4. S26 Ultra")
    print("5. Sair")

opcao = int(input("Digite a linha de celular: "))
if opcao == 1:
    xiomi()
    escolha = int(input("Digite o número do celular que deseja comprar: "))
    if escolha == 1:
        print("Você escolheu o Xiomi Redmi Note 11 Pro")
    elif escolha == 2:
        print("Você escolheu o Xiomi Redmi Note 12 Pro Plus")
    elif escolha == 3:
        print("Você escolheu o Xiomi Redmi Note 15 Pro Max")
    elif escolha == 4:
        print("Você escolheu o Xiomi Redmi Note 14 Pro Ultra")
    elif escolha == 5:
        print("Saindo...")
    else:
        print("Opção inválida.")
elif opcao == 2:
    iphone()
    escolha = int(input("Digite o número do celular que deseja comprar: "))
    if escolha == 1:
        print("Você escolheu o Iphone 15 Pro Max")
    elif escolha == 2:
        print("Você escolheu o Iphone 15 Pro")
    elif escolha == 3:
        print("Você escolheu o Iphone X")
    elif escolha == 4:
        print("Você escolheu o Iphone 11")
    elif escolha == 5:
        print("Saindo...")
    else:
        print("Opção inválida.")
elif opcao == 3:
    samsung()
    escolha = int(input("Digite o número do celular que deseja comprar: "))
    if escolha == 1:
        print("Você escolheu o Samsung Galaxy S24 Ultra")
    elif escolha == 2:
        print("Você escolheu o S26 Plus")
    elif escolha == 3:
        print("Você escolheu o S26 Ultra")
    elif escolha == 4:
        print("Saindo...")
    else:
        print("Opção inválida.")
