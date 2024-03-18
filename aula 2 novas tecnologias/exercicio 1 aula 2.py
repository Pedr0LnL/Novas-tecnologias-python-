def adicao():
    print("\n--- Tabuada de Adição ---")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} + {j} = {i + j}")
        print()

def subtracao():
    print("\n--- Tabuada de Subtração ---")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} - {j} = {i - j}")
        print()

def multiplicacao():
    print("\n--- Tabuada de Multiplicação ---")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

def divisao():
    print("\n--- Tabuada de Divisão ---")
    for i in range(1, 11):
        for j in range(1, 11):
            if j != 0:
                print(f"{i} / {j} = {i / j}")
            else:
                print(f"{i} / {j} = Indefinido")
        print()

def main():
    while True:
        # Exibe o menu de opções
        print("\nMenu:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        # Solicita ao usuário que escolha uma opção
        escolha = input("Escolha uma opção: ")

        # Realiza a operação conforme a escolha do usuário
        if escolha == "1":
            adicao()
        elif escolha == "2":
            subtracao()
        elif escolha == "3":
            multiplicacao()
        elif escolha == "4":
            divisao()
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
