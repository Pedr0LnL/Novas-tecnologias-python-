import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'algoritmo', 'dados', 'desenvolvimento']
    return random.choice(palavras)

def jogar_forca(palavra):
    letras_corretas = []
    letras_erradas = []
    chances = 6

    while chances > 0:
        palavra_descoberta = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_descoberta += letra
            else:
                palavra_descoberta += '_'

        print("\nPalavra: ", palavra_descoberta)
        print("Letras erradas: ", letras_erradas)
        print("Chances restantes: ", chances)

        if palavra_descoberta == palavra:
            print("\nParabéns! Você acertou a palavra:", palavra)
            break

        letra_usuario = input("\nDigite uma letra: ").lower()

        if letra_usuario in palavra:
            letras_corretas.append(letra_usuario)
        else:
            letras_erradas.append(letra_usuario)
            chances -= 1

    else:
        print("\nVocê perdeu! A palavra era:", palavra)

def main():
    print("Bem-vindo ao Jogo da Forca!")
    palavra = escolher_palavra()
    jogar_forca(palavra)

if __name__ == "__main__":
    main()
