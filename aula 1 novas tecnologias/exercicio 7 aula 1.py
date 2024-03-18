def celsius_para_fahrenheit(celsius):
    # Fórmula de conversão de Celsius para Fahrenheit
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    # Solicita ao usuário que insira a temperatura em Celsius
    celsius = float(input("Digite a temperatura em Celsius: "))

    # Converte a temperatura de Celsius para Fahrenheit
    fahrenheit = celsius_para_fahrenheit(celsius)

    # Imprime o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit)

if __name__ == "__main__":
    main()
