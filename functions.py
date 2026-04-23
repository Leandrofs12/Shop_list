
def remover_item(lista):
    exibir_lista(lista)
    if lista:
        try:
            indice = int(input("Digite o número do item para remover: ")) - 1
            removido = lista.pop(indice)
            print(f"❌ {removido} removido!")
        except (ValueError, IndexError):
            print("Número inválido!")
            