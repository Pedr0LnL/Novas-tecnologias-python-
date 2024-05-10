class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.associacoes = []

    def adicionar_associacao(self, disciplina, professor, sala_de_aula):
        self.associacoes.append({"disciplina": disciplina, "professor": professor, "sala_de_aula": sala_de_aula})

    def consultar_associacoes(self):
        return self.associacoes



class Professor:
    def __init__(self, nome, idade, disciplinas):
        self.nome = nome
        self.idade = idade
        self.disciplinas = disciplinas

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade

    def consultar_disciplinas(self):
        return self.disciplinas


class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo


class SalaDeAula:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade


class SistemaGerenciador:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        self.salas_de_aula = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def adicionar_sala_de_aula(self, sala_de_aula):
        self.salas_de_aula.append(sala_de_aula)

    def associar_aluno_disciplina(self, aluno, disciplina):
        aluno.adicionar_disciplina(disciplina)

    def associar_aluno_sala(self, aluno, sala_de_aula):
        aluno.associar_sala_de_aula(sala_de_aula)

    def associar_aluno_professor(self, aluno, nome_professor):
        for professor in self.professores:
            if professor.nome == nome_professor:
                return professor
        return None


    def consultar_alunos(self):
        return self.alunos

    def consultar_professores(self):
        return self.professores

    def consultar_disciplinas(self):
        return self.disciplinas

    def consultar_salas_de_aula(self):
        return self.salas_de_aula


# Função para registrar um aluno
def registrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    matricula = input("Matrícula do aluno: ")
    return Aluno(nome, idade, matricula)


# Função para registrar um professor
def registrar_professor(sistema):
    nome = input("Nome do professor: ")
    idade = int(input("Idade do professor: "))
    disciplinas = input("Disciplinas do professor (separadas por vírgula): ").split(",")
    return Professor(nome, idade, disciplinas)



# Função para registrar uma disciplina
def registrar_disciplina():
    nome = input("Nome da disciplina: ")
    codigo = input("Código da disciplina: ")
    return Disciplina(nome, codigo)


# Função para registrar uma sala de aula
def registrar_sala_de_aula():
    numero = input("Número da sala de aula: ")
    capacidade = int(input("Capacidade da sala de aula: "))
    return SalaDeAula(numero, capacidade)


# Exemplo de uso do sistema:
sistema = SistemaGerenciador()

while True:
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
    print("11. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aluno = registrar_aluno()
        sistema.adicionar_aluno(aluno)
        print("Aluno registrado com sucesso!")
    elif opcao == "2":
        professor = registrar_professor(sistema)
        sistema.adicionar_professor(professor)
        print(f"Professor {professor.nome} registrado com sucesso!")
    elif opcao == "3":
        disciplina = registrar_disciplina()
        sistema.adicionar_disciplina(disciplina)
        print("Disciplina registrada com sucesso!")
    elif opcao == "4":
        sala_de_aula = registrar_sala_de_aula()
        sistema.adicionar_sala_de_aula(sala_de_aula)
        print("Sala de aula registrada com sucesso!")
    elif opcao == "5":
        alunos = sistema.consultar_alunos()
        disciplinas = sistema.consultar_disciplinas()
        salas_de_aula = sistema.consultar_salas_de_aula()
    
        if alunos:  # Verifica se a lista de alunos não está vazia
            aluno_nome = input("Nome do aluno: ")
            aluno_encontrado = False
            for aluno in alunos:
                if aluno.nome == aluno_nome:
                    aluno_encontrado = True
                    disciplina_nome = input("Nome da disciplina: ")
                    disciplina_encontrada = False
                    for disciplina in disciplinas:
                        if disciplina.nome == disciplina_nome:
                            disciplina_encontrada = True
                            sala_nome = input("Nome da sala de aula: ")
                            sala_encontrada = False
                            for sala in salas_de_aula:
                                if sala.numero == sala_nome:
                                    sala_encontrada = True
                                    nome_professor = input("Nome do professor: ")
                                
                                    if sistema.associar_aluno_professor(aluno, nome_professor):
                                        professor = sistema.associar_aluno_professor(aluno, nome_professor)
                                        aluno.adicionar_associacao(disciplina, professor, sala)  # Adicionar associação ao aluno
                                        print("Aluno associado a disciplina, sala de aula e professor com sucesso!")
                                    else:
                                        print("Professor não encontrado!")

                                    break  # Sai do loop depois de encontrar a sala de aula
                            if not sala_encontrada:
                                print("Sala de aula não encontrada.")
                            break  # Sai do loop depois de encontrar a disciplina
                    if not disciplina_encontrada:
                        print("Disciplina não encontrada.")
                    break  # Sai do loop depois de encontrar o aluno
            if not aluno_encontrado:
                print("Aluno não encontrado.")
        else:
            print("Não há alunos registrados!")

    elif opcao == "6":
        print("\nAssociações Registradas:")
        for aluno in sistema.consultar_alunos():
            print(f"Aluno: {aluno.nome}")
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
            print(professor.nome)
    elif opcao == "9":
        print("\nDisciplinas:")
        for disciplina in sistema.consultar_disciplinas():
            print(disciplina.nome, disciplina.codigo)
    elif opcao == "10":
        print("\nSalas de Aula:")
        for sala in sistema.consultar_salas_de_aula():
            print("Sala:", sala.numero, "Capacidade:", sala.capacidade)
    elif opcao == "11":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

