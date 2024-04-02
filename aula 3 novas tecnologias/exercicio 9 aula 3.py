def comparar_listas_versoes(lista_inicial, lista_modificada):
    # Converte as listas em conjuntos para facilitar a comparação
    set_inicial = set(lista_inicial)
    set_modificada = set(lista_modificada)

    # Elementos que não mudaram
    nao_mudaram = set_inicial.intersection(set_modificada)

    # Novos elementos
    novos_elementos = set_modificada - set_inicial

    # Elementos removidos
    removidos = set_inicial - set_modificada

    return nao_mudaram, novos_elementos, removidos

# Função principal
def main():
    lista_inicial = [1, 2, 3, 4, 5]
    lista_modificada = [2, 3, 5, 6, 7]

    nao_mudaram, novos_elementos, removidos = comparar_listas_versoes(lista_inicial, lista_modificada)

    print("Elementos que não mudaram:", nao_mudaram)
    print("Novos elementos:", novos_elementos)
    print("Elementos removidos:", removidos)

if __name__ == "__main__":
    main()
