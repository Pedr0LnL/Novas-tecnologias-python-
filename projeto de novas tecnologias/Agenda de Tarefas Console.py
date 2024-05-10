import os

def exibir_menu():
    print("=== Agenda de Tarefas ===")
    print("1. Visualizar Tarefas")
    print("2. Adicionar Tarefa")
    print("3. Remover Tarefa")
    print("4. Sair")

def visualizar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
            if tarefas:
                print("Tarefas:")
                for index, tarefa in enumerate(tarefas, start=1):
                    print(f"{index}. {tarefa.strip()}")
            else:
                print("Nenhuma tarefa encontrada.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    with open("tarefas.txt", "a") as arquivo:
        arquivo.write(tarefa + "\n")
    print("Tarefa adicionada com sucesso.")

def remover_tarefa():
    visualizar_tarefas()
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
        indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(tarefas)
            print(f"Tarefa '{tarefa_removida.strip()}' removida com sucesso.")
        else:
            print("Índice inválido.")
    except (ValueError, IndexError):
        print("Índice inválido.")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            visualizar_tarefas()
        elif opcao == "2":
            adicionar_tarefa()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo da agenda.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    if not os.path.exists("tarefas.txt"):
        with open("tarefas.txt", "w"):
            pass
    main()
