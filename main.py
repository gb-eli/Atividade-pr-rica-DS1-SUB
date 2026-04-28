import andre
import chapaval
import clara
import diego
import eduardamenna
import gustavofurtado
import marelis
import mariolobo

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Andre       (Hamburguer)")
        print("2 - Chapaval    (Carrinho de compras)")
        print("3 - Clara       (Pizza)")
        print("4 - Diego       (Roupas)")
        print("5 - Eduarda     (Login/Cadastro)")
        print("6 - Gustavo     (Celulares)")
        print("7 - Marelis     (Venda)")
        print("8 - Mario Lobo  (Frutas)")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            andre.menu()
        elif opcao == "2":
            chapaval.menu()
        elif opcao == "3":
            clara.menu()
        elif opcao == "4":
            diego.menu_roupas()
        elif opcao == "5":
            eduardamenna.menu()
        elif opcao == "6":
            gustavofurtado.menu()
        elif opcao == "7":
            marelis.Venda()
        elif opcao == "8":
            mariolobo.menu()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu_principal()
