def comparar_listas(lista1, lista2):
    # Converte as listas em conjuntos para facilitar a comparação
    set1 = set(lista1)
    set2 = set(lista2)

    # Valores comuns às duas listas
    comuns = set1.intersection(set2)

    # Valores que existem apenas na primeira lista
    apenas_na_primeira = set1 - set2

    # Valores que existem apenas na segunda lista
    apenas_na_segunda = set2 - set1

    # Lista com os elementos não repetidos das duas listas
    elementos_unicos = list(set1.union(set2))

    # Primeira lista sem os elementos repetidos na segunda
    sem_repetidos_na_segunda = list(set1 - set2)

    return comuns, apenas_na_primeira, apenas_na_segunda, elementos_unicos, sem_repetidos_na_segunda

# Função principal
def main():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]

    comuns, apenas_na_primeira, apenas_na_segunda, elementos_unicos, sem_repetidos_na_segunda = comparar_listas(lista1, lista2)

    print("Valores comuns às duas listas:", comuns)
    print("Valores que só existem na primeira lista:", apenas_na_primeira)
    print("Valores que só existem na segunda lista:", apenas_na_segunda)
    print("Lista com elementos não repetidos das duas listas:", elementos_unicos)
    print("Primeira lista sem os elementos repetidos na segunda:", sem_repetidos_na_segunda)

if __name__ == "__main__":
    main()
