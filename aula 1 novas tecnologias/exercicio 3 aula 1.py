def main():
    # Solicitar ao usuário para inserir um número inteiro
    num = int(input("Insira um número inteiro: "))

    # Verificar se o número é par ou ímpar e imprimir o resultado
    if num % 2 == 0:
        print(f"{num} é um número par.")
    else:
        print(f"{num} é um número ímpar.")

if __name__ == "__main__":
    main()
