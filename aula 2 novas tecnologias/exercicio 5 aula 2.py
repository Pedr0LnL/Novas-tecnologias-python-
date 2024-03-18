def calcular_quadrado_com_soma_impares(n):
    if n == 1:
        return 1
    
    soma_impares = 1
    numero_impar = 1

    for _ in range(2, n + 1):
        numero_impar += 2
        soma_impares += numero_impar
    
    return soma_impares

def main():
    numero = int(input("Digite um número natural: "))
    
    if numero < 1:
        print("Por favor, insira um número natural maior ou igual a 1.")
    else:
        quadrado = calcular_quadrado_com_soma_impares(numero)
        print(f"O quadrado de {numero} é: {quadrado}")

if __name__ == "__main__":
    main()
