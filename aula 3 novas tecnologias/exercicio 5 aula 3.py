V = [9, 8, 7, 12, 0, 13, 21]
pares = []
impares = []

for valor in V:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Valores pares:", pares)
print("Valores ímpares:", impares)
