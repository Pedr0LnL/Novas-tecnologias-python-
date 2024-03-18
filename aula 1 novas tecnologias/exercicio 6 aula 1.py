def converter_segundos(tempo_em_segundos):
    # Calcula o número de dias, horas, minutos e segundos
    dias = tempo_em_segundos // (24 * 3600)
    tempo_em_segundos %= (24 * 3600)
    horas = tempo_em_segundos // 3600
    tempo_em_segundos %= 3600
    minutos = tempo_em_segundos // 60
    segundos = tempo_em_segundos % 60
    return dias, horas, minutos, segundos

def main():
    # Solicita ao usuário que insira a quantidade de segundos
    segundos = int(input("Digite a quantidade de segundos: "))

    # Chama a função para converter segundos em dias, horas, minutos e segundos
    dias, horas, minutos, segundos_restantes = converter_segundos(segundos)

    # Imprime o resultado
    print("Dias:", dias)
    print("Horas:", horas)
    print("Minutos:", minutos)
    print("Segundos:", segundos_restantes)

if __name__ == "__main__":
    main()
