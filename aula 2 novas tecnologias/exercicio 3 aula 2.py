def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primeiros_n_primos(n):
    numeros_primos = []
    numero = 2
    while len(numeros_primos) < n:
        if eh_primo(numero):
            numeros_primos.append(numero)
        numero += 1
    return numeros_primos

def main():
    n = int(input("Digite a quantidade de números primos que você deseja encontrar: "))
    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
        return
    primeiros_primos = primeiros_n_primos(n)
    print(f"Os primeiros {n} números primos são:")
    print(primeiros_primos)

if __name__ == "__main__":
    main()
