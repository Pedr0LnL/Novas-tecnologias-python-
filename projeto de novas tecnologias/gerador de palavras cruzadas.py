import random

def generate_crossword(words):
    # Encontra a palavra mais longa na lista
    max_length = max(len(word) for word in words)
    
    # Inicializa a grade de palavras cruzadas
    grid = [[' ' for _ in range(max_length)] for _ in range(max_length)]
    
    # Lista para acompanhar as palavras colocadas
    placed_words = []
    
    # Função para verificar se uma palavra pode ser colocada em uma posição específica
    def can_place(word, row, col, vertical):
        if vertical:
            return all(grid[row+i][col] == ' ' or grid[row+i][col] == word[i] for i in range(len(word)))
        else:
            return all(grid[row][col+i] == ' ' or grid[row][col+i] == word[i] for i in range(len(word)))
    
    # Função para colocar uma palavra em uma posição específica
    def place_word(word, row, col, vertical):
        if vertical:
            for i in range(len(word)):
                grid[row+i][col] = word[i]
        else:
            for i in range(len(word)):
                grid[row][col+i] = word[i]
    
    # Coloca as palavras na grade horizontal e verticalmente
    for word in words:
        placed = False
        while not placed:
            # Escolhe aleatoriamente entre colocar horizontal ou verticalmente
            vertical = random.choice([True, False])
            
            if vertical:
                row = random.randint(0, max_length - len(word))
                col = random.randint(0, max_length - 1)
            else:
                row = random.randint(0, max_length - 1)
                col = random.randint(0, max_length - len(word))
            
            # Verifica se a posição escolhida está livre
            if can_place(word, row, col, vertical):
                place_word(word, row, col, vertical)
                placed_words.append((word, row, col, vertical))
                placed = True
    
    return grid, placed_words

def display_crossword(grid):
    for row in grid:
        print(' '.join(row))

if __name__ == "__main__":
    word_list = input("Digite as palavras separadas por vírgula: ").split(',')
    crossword_grid, placed_words = generate_crossword(word_list)
    print("Palavras Cruzadas:")
    display_crossword(crossword_grid)
    print("\nPalavras colocadas:")
    for word, row, col, vertical in placed_words:
        direction = "vertical" if vertical else "horizontal"
        print(f"{word}: linha {row+1}, coluna {col+1}, direção {direction}")
