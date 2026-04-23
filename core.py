def carregar_itens():
    try:
        with open("lista_compras.txt", "r") as f:
            return [linha.strip() for linha in f.readlines()]
    except FileNotFoundError:
        return []

def salvar_itens(lista):
    with open("lista_compras.txt", "w") as f:
        for item in lista:
            f.write(f"{item}\n")