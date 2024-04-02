# Criando dicionários para representar os animais de estimação
animal1 = {
    'nome': 'Bolinha',
    'tipo': 'Cachorro',
    'dono': 'João'
}

animal2 = {
    'nome': 'Whiskas',
    'tipo': 'Gato',
    'dono': 'Maria'
}

animal3 = {
    'nome': 'Floquinho',
    'tipo': 'Coelho',
    'dono': 'Carlos'
}

# Armazenando os dicionários dos animais de estimação em uma lista
pets = [animal1, animal2, animal3]

# Percorrendo a lista de animais de estimação e apresentando todas as informações sobre cada um
for pet in pets:
    print("Informações sobre o animal de estimação:")
    print("Nome:", pet['nome'])
    print("Tipo:", pet['tipo'])
    print("Dono:", pet['dono'])
    print()  # Adiciona uma linha em branco entre as informações de cada animal de estimação
