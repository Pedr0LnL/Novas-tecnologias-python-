lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# a. Imprimir o maior elemento
maior_elemento = max(lista)
print("Maior elemento:", maior_elemento)

# b. Imprimir o menor elemento
menor_elemento = min(lista)
print("Menor elemento:", menor_elemento)

# c. Imprimir os números pares
numeros_pares = [num for num in lista if num % 2 == 0]
print("Números pares:", numeros_pares)

# d. Imprimir o número de ocorrências do primeiro elemento da lista
ocorrencias_primeiro_elemento = lista.count(lista[0])
print("Número de ocorrências do primeiro elemento:", ocorrencias_primeiro_elemento)

# e. Imprimir a média dos elementos
media_elementos = sum(lista) / len(lista)
print("Média dos elementos:", media_elementos)

# f. Imprimir a soma dos elementos de valor negativo
soma_negativos = sum(num for num in lista if num < 0)
print("Soma dos elementos de valor negativo:", soma_negativos)
