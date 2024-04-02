def contar_caracteres(frase):
    # Inicializa o dicionário vazio
    contador = {}
    
    # Percorre cada caractere na frase
    for char in frase:
        # Incrementa o contador para esse caractere
        contador[char] = contador.get(char, 0) + 1
    
    return contador

# Função para remover espaços e tornar a frase em minúsculas
def preprocessar_frase(frase):
    return frase.replace(" ", "").lower()

# Função principal
def main():
    frase = input("Digite uma frase: ")
    frase_preprocessada = preprocessar_frase(frase)
    resultado = contar_caracteres(frase_preprocessada)
    print("Contagem de caracteres:")
    print(resultado)

if __name__ == "__main__":
    main()
