
def exibir_lista(lista):
    print("\n--- SUA LISTA DE COMPRAS ---")
    if not lista:
        print("A lista está vazia.")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")
    print("---------------------------\n")
    