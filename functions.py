def adicionar_item(lista):
    item = input("Digite o nome do produto: ")
    qtd = input("Digite a quantidade: ")
    lista.append(f"{item} ({qtd})")
    print("✔ Item adicionado!")