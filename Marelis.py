def Venda(): 
    print("=== VENDA ===")
    print("1 - REFRIGERANTE")
    print("2 - LANCHE")
    print("3 - AÇAI")

    pedido = input("Escolha uma opção do cardápio: ")
    if pedido == "1":
        print("você escolheu refrigerante")
    elif pedido == "2":
        print("você escolheu lanche")
    elif pedido == "3":
        print("você escolheu açaí")
    else:
        print("NÃO TEM ESSA OPÇÃO")

Venda()