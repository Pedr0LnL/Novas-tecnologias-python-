def calcular_digito_verificador(numero_conta):
    soma = sum(int(digito) for digito in numero_conta)
    digito_verificador = (10 - (soma % 10)) % 10
    return digito_verificador

def numero_conta_completo(numero_conta):
    digito_verificador = calcular_digito_verificador(numero_conta)
    numero_completo = f"00{numero_conta}-{digito_verificador}"
    return numero_completo

def main():
    numero_conta = input("Digite o número da conta (até 6 dígitos): ")
    if not numero_conta.isdigit() or len(numero_conta) > 6:
        print("Por favor, insira um número de conta válido.")
    else:
        conta_completa = numero_conta_completo(numero_conta)
        print("Número de conta completo:", conta_completa)

if __name__ == "__main__":
    main()
