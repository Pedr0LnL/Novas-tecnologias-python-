def main():
    # Solicitar ao usuário para inserir um número de cinco dígitos
    numero = input("Insira um número de cinco dígitos: ")

    # Verificar se o número tem exatamente cinco dígitos
    if len(numero) != 5:
        print("Por favor, insira um número de cinco dígitos.")
        return

    # Separar o número em dígitos individuais e imprimir separados por três espaços
    for digito in numero:
        print(digito, end="   ")

if __name__ == "__main__":
    main()
