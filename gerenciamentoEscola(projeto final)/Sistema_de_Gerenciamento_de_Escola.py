from escola.sistema_gerenciador import SistemaGerenciador

sistema = SistemaGerenciador()
pula_espera=0
while True:
    if pula_espera != 0:espera = input("Aperte enter para continuar")
    pula_espera+=1
    print("\nOpções:")
    print("1. Registrar Aluno")
    print("2. Registrar Professor")
    print("3. Registrar Disciplina")
    print("4. Registrar Sala de Aula")
    print("5. Registrar Grade de Aula")
    print("6. Visualizar Grade de Aula")
    print("7. Consultar Alunos")
    print("8. Consultar Professores")
    print("9. Consultar Disciplinas")
    print("10. Consultar Salas de Aula")
    print("11. editar Alunos")
    print("12. editar Professores")
    print("13. editar Disciplinas")
    print("14. editar Salas de Aula")
    print("15. editar Grade de Aula")
    print("16. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aluno = sistema.registrar_aluno()
        print("Aluno registrado com sucesso!")
    elif opcao == "2":
        professor = sistema.registrar_professor()
        print(f"Professor {professor.nome} registrado com sucesso!")
    elif opcao == "3":
        disciplina = sistema.registrar_disciplina()
        print("Disciplina registrada com sucesso!")
    elif opcao == "4":
        sala_de_aula = sistema.registrar_sala_de_aula()
        print("Sala de aula registrada com sucesso!")
    elif opcao == "5":
        sistema.registrar_grade_aula()

    elif opcao == "6":
        print("\nAssociações Registradas:")
        for aluno in sistema.consultar_alunos():
            print(f"Aluno: {aluno.nome}")
            if aluno.associacoes != True:
                print("- Disciplinas:")
                for associacao in aluno.associacoes:
                    print(f"  - {associacao['disciplina'].nome}")
                    print(f"- Sala de Aula: {associacao['sala_de_aula'].numero}")
                    print(f"- Professor: {associacao['professor'].nome}")
                print()
    elif opcao == "7":
        print("\nAlunos:")
        for aluno in sistema.consultar_alunos():
            print(aluno.nome, aluno.matricula)
    elif opcao == "8":
        print("\nProfessores:")
        for professor in sistema.consultar_professores():
            print(f"Nome: {professor.nome}, Idade: {professor.idade}")
            if professor.disciplinas:
                print("Disciplinas:")
                for disciplina in professor.disciplinas:
                    print(f" - {disciplina.nome} ({disciplina.codigo})")
            else:
                print(" - Nenhuma disciplina associada.")
    elif opcao == "9":
        print("\nDisciplinas:")
        for disciplina in sistema.consultar_disciplinas():
            print(disciplina.nome, disciplina.codigo)
    elif opcao == "10":
        print("\nSalas de Aula:")
        for sala in sistema.consultar_salas_de_aula():
            print("Sala:", sala.numero, "Capacidade:", sala.capacidade)
    elif opcao == "11":
        print("\nAlunos:")
        for aluno in sistema.consultar_alunos():
            print(aluno.nome, aluno.matricula)
        nome_aluno = input("Nome do aluno a ser editado: ")
        sistema.editar_aluno(nome_aluno)
    elif opcao == "12":
        print("\nProfessores:")
        for professor in sistema.consultar_professores():
            print(f"Nome: {professor.nome}, Idade: {professor.idade}")
            if professor.disciplinas:
                print("Disciplinas:")
                for disciplina in professor.disciplinas:
                    print(f" - {disciplina.nome} ({disciplina.codigo})")
            else:
                print(" - Nenhuma disciplina associada.")
        nome_professor = input("Digite o nome do professor que deseja editar: ")
        sistema.edita_professor(nome_professor)
        print("Professor editado com sucesso!")
    elif opcao == "13":
        print("\nDisciplinas:")
        for disciplina in sistema.consultar_disciplinas():
            print(disciplina.nome, disciplina.codigo)
        nome_disciplina = input("Nome da disciplina a ser editada: ")
        sistema.editar_disciplina(nome_disciplina)
    elif opcao == "14":
        print("\nSalas de Aula:")
        for sala in sistema.consultar_salas_de_aula():
            print("Sala:", sala.numero, "Capacidade:", sala.capacidade)
        numero_sala = input("Número da sala de aula a ser editada: ")
        sistema.editar_sala_de_aula(numero_sala)
    elif opcao == "15":
        print("\nAlunos:")
        for aluno in sistema.consultar_alunos():
            print(aluno.nome, aluno.matricula)
        aluno_nome = input("Nome do aluno para editar grade de aula: ")
        sistema.editar_grade_aula(aluno_nome)
    elif opcao == "16":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

