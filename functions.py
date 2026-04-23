
def remover_item(lista):
    exibir_lista(lista)
    if lista:
        try:
            indice = int(input("Digite o número do item para remover: ")) - 1
            removido = lista.pop(indice)
            print(f"❌ {removido} removido!")
        except (ValueError, IndexError):
            print("Número inválido!")
            
def exibir_lista(lista):
    print("\n--- SUA LISTA DE COMPRAS ---")
    if not lista:
        print("A lista está vazia.")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")
    print("---------------------------\n")
    
def adicionar_item(lista):
    item = input("Digite o nome do produto: ")
    qtd = input("Digite a quantidade: ")
    lista.append(f"{item} ({qtd})")
    print("✔ Item adicionado!")
