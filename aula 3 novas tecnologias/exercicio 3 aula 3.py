def verifica_parentheses(expressao):
    pilha = []
    abre_parenteses = '({['
    fecha_parenteses = ')}]'

    for caractere in expressao:
        if caractere in abre_parenteses:
            pilha.append(caractere)
        elif caractere in fecha_parenteses:
            if not pilha:
                return False
            topo = pilha.pop()
            if abre_parenteses.index(topo) != fecha_parenteses.index(caractere):
                return False

    return len(pilha) == 0

expressao = input("Digite a expressão com parênteses: ")
if verifica_parentheses(expressao):
    print("Os parênteses foram abertos e fechados corretamente.")
else:
    print("Erro! Os parênteses não foram abertos e fechados corretamente.")
