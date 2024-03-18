def calcular_raizes(a, b, c):
    # Calculando o discriminante
    delta = b**2 - 4*a*c

    # Verificando a natureza das raízes com base no discriminante
    if delta > 0:
        # Duas raízes reais e distintas
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1, x2
    elif delta == 0:
        # Raízes reais iguais
        x = -b / (2*a)
        return x, x
    else:
        # Raízes complexas
        parte_real = -b / (2*a)
        parte_imaginaria = (-delta)**0.5 / (2*a)
        x1 = complex(parte_real, parte_imaginaria)
        x2 = complex(parte_real, -parte_imaginaria)
        return x1, x2

def main():
    # Solicitar ao usuário os coeficientes da equação do segundo grau
    a = float(input("Digite o coeficiente 'a': "))
    b = float(input("Digite o coeficiente 'b': "))
    c = float(input("Digite o coeficiente 'c': "))

    # Calcular as raízes
    raiz1, raiz2 = calcular_raizes(a, b, c)

    # Imprimir as raízes
    print("As raízes da equação são:")
    print("x' =", raiz1)
    print("x'' =", raiz2)

if __name__ == "__main__":
    main()
