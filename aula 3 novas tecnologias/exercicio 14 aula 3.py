def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)


def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True

    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True

    return False


def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        print_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1

            if verificar_vencedor(tabuleiro, jogador_atual):
                print_tabuleiro(tabuleiro)
                print(f"Parabéns! Jogador {jogador_atual} venceu!")
                break
            elif jogadas == 9:
                print_tabuleiro(tabuleiro)
                print("Empate!")
                break
            else:
                jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já foi escolhida. Escolha outra.")

jogar_jogo_da_velha()
