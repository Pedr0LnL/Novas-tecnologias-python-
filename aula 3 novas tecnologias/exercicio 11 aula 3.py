# Informações sobre a primeira pessoa
pessoa1 = {
    'first_name': 'João',
    'last_name': 'Silva',
    'age': 30,
    'city': 'São Paulo'
}

# Informações sobre a segunda pessoa
pessoa2 = {
    'first_name': 'Maria',
    'last_name': 'Santos',
    'age': 25,
    'city': 'Rio de Janeiro'
}

# Armazenando os dicionários das pessoas em uma lista
people = [pessoa1, pessoa2]

# Percorrendo a lista de pessoas e apresentando todas as informações sobre cada uma
for pessoa in people:
    print("Informações sobre a pessoa:")
    print("Primeiro nome:", pessoa['first_name'])
    print("Sobrenome:", pessoa['last_name'])
    print("Idade:", pessoa['age'])
    print("Cidade:", pessoa['city'])
    print()  # Adiciona uma linha em branco entre as informações de cada pessoa
