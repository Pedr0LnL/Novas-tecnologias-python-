def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

def main():
    numero = int(input("Digite um número não negativo: "))
    
    if numero < 0:
        print("Por favor, insira um número não negativo.")
    else:
        fatorial = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é: {fatorial}")

if __name__ == "__main__":
    main()
