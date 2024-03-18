def fibonacci(n):
    if n <= 0:
        return "Por favor, insira um número inteiro maior que 0."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

def main():
    n = int(input("Digite o valor de n (n >= 3): "))
    resultado = fibonacci(n)
    print(f"O {n}-ésimo termo da sequência de Fibonacci é: {resultado}")

if __name__ == "__main__":
    main()
