def main():
    # Solicitar ao usuário para inserir dois inteiros
    num1 = int(input("Insira o primeiro inteiro: "))
    num2 = int(input("Insira o segundo inteiro: "))

    # Calcular e imprimir a soma, produto, diferença e divisão
    soma = num1 + num2
    produto = num1 * num2
    diferenca = num1 - num2
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Não é possível dividir por zero."

    print("Soma:", soma)
    print("Produto:", produto)
    print("Diferença:", diferenca)
    print("Divisão:", divisao)

if __name__ == "__main__":
    main()
