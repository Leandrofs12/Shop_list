from core import carregar_itens, salvar_itens
from functions import adicionar_item, exibir_lista, remover_item

def menu():
    lista = carregar_itens()
    
    while True:
        print("1. Adicionar | 2. Listar | 3. Remover | 4. Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            adicionar_item(lista)
        elif opcao == "2":
            exibir_lista(lista)
        elif opcao == "3":
            remover_item(lista)
        elif opcao == "4":
            salvar_itens(lista)
            print("Lista salva. Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()