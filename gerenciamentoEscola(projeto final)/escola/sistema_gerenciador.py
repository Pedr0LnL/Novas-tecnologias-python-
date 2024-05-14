from escola.aluno import Aluno
from escola.professor import Professor
from escola.disciplina import Disciplina
from escola.sala_de_aula import SalaDeAula

class SistemaGerenciador:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        self.salas_de_aula = []

    def registrar_aluno(self):
        nome = input("Nome do aluno: ")
        idade = int(input("Idade do aluno: "))
        matricula = input("Matrícula do aluno: ")
        aluno = Aluno(nome, idade, matricula)
        self.alunos.append(aluno)
        return aluno

    def registrar_professor(self):
        nome = input("Nome do professor: ")
        idade = int(input("Idade do professor: "))
        professor = Professor(nome, idade)
        self.professores.append(professor)
        print("Deseja registrar uma disciplina?")
        print("1. Registrar disciplina")
        print("2. Não")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            self.mostrar_disciplinas()
            codigo_disciplina = input("Digite o código da disciplina que deseja associar ao professor: ")
            disciplina_encontrada = None
            for disciplina in self.disciplinas:
                if disciplina.codigo == codigo_disciplina:
                    disciplina_encontrada = disciplina
                    break
            if disciplina_encontrada:
                professor.adicionar_disciplina(disciplina_encontrada)
                print(f"Professor {professor.nome} associado à disciplina {disciplina_encontrada.nome} com sucesso!")
            else:
                print("Código de disciplina inválido.")

        return professor

    def registrar_disciplina(self):
        nome = input("Nome da disciplina: ")
        codigo = input("Código da disciplina: ")
        disciplina = Disciplina(nome, codigo)
        self.disciplinas.append(disciplina)
        return disciplina

    def registrar_sala_de_aula(self):
        numero = input("Número da sala de aula: ")
        capacidade = int(input("Capacidade da sala de aula: "))
        sala_de_aula = SalaDeAula(numero, capacidade)
        self.salas_de_aula.append(sala_de_aula)
        return sala_de_aula
    
    def registrar_grade_aula(self):
        print("\nAlunos disponíveis:")
        for aluno in self.consultar_alunos():
            print(aluno.nome)

        print("\nDisciplinas disponíveis:")
        for disciplina in self.consultar_disciplinas():
            print(disciplina.nome)

        print("\nSalas de aula disponíveis:")
        for sala in self.consultar_salas_de_aula():
            print("Sala:", sala.numero, "Capacidade:", sala.capacidade)

        print("\nProfessores disponíveis:")
        for professor in self.consultar_professores():
            print(f"Professor: {professor.nome}, Idade: {professor.idade}")

        alunos = self.consultar_alunos()
        disciplinas = self.consultar_disciplinas()
        salas_de_aula = self.consultar_salas_de_aula()

        if alunos:
            aluno_nome = input("\nNome do aluno: ")
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

                                    if self.associar_aluno_professor(aluno, nome_professor):
                                        professor = self.associar_aluno_professor(aluno, nome_professor)
                                        aluno.adicionar_associacao(disciplina, professor, sala)
                                        print("Aluno associado a disciplina, sala de aula e professor com sucesso!")
                                    else:
                                        print("Professor não encontrado!")

                                    break
                            if not sala_encontrada:
                                print("Sala de aula não encontrada.")
                            break
                    if not disciplina_encontrada:
                        print("Disciplina não encontrada.")
                    break
            if not aluno_encontrado:
                print("Aluno não encontrado.")
        else:
            print("Não há alunos registrados!")
    
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
    
    def mostrar_disciplinas(self):
        if self.disciplinas:
            print("Disciplinas cadastradas:")
            for disciplina in self.disciplinas:
                print(f"Nome: {disciplina.nome} - Código: {disciplina.codigo}")
        else:
            print("Não há disciplinas cadastradas.")

    def editar_aluno(self, nome_aluno):
        for aluno in self.alunos:
            if aluno.nome == nome_aluno:
                novo_nome = input("Novo nome do aluno: ")
                nova_idade = int(input("Nova idade do aluno: "))
                nova_matricula = input("Nova matrícula do aluno: ")

                aluno.nome = novo_nome
                aluno.idade = nova_idade
                aluno.matricula = nova_matricula

                print("Aluno editado com sucesso!")
                return
        print("Aluno não encontrado.")

    def edita_professor(self, nome_antigo):
        for professor in self.professores:
            if professor.nome == nome_antigo:
                novo_nome = input("Novo nome do professor: ")
                nova_idade = int(input("Nova idade do professor: "))
                professor.atualizar_info(novo_nome, nova_idade)

                print("Deseja adicionar ou remover uma disciplina ao professor?")
                print("1. Adicionar disciplina")
                print("2. Remover disciplina")
                print("3. Não fazer alterações nas disciplinas")
                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    self.mostrar_disciplinas()
                    codigo_disciplina = input("Digite o código da disciplina que deseja associar ao professor: ")
                    disciplina_encontrada = None
                    for disciplina in self.disciplinas:
                        if disciplina.codigo == codigo_disciplina:
                            disciplina_encontrada = disciplina
                            break
                    if disciplina_encontrada:
                        professor.adicionar_disciplina(disciplina_encontrada)
                        print(f"Disciplina {disciplina_encontrada.nome} adicionada ao professor {professor.nome} com sucesso!")
                    else:
                        print("Código de disciplina inválido.")
                elif opcao == "2":
                    codigo_disciplina = input("Digite o código da disciplina que deseja remover do professor: ")
                    if professor.remover_disciplina(codigo_disciplina):
                        print(f"Disciplina removida do professor {professor.nome} com sucesso!")
                    else:
                        print("Disciplina não encontrada.")
                elif opcao != "3":
                    print("Opção inválida.")
                return
        print("Professor não encontrado.")

    def editar_disciplina(self, nome_disciplina):
        for disciplina in self.disciplinas:
            if disciplina.nome == nome_disciplina:
                novo_nome = input("Novo nome da disciplina: ")
                novo_codigo = input("Novo código da disciplina: ")

                disciplina.nome = novo_nome
                disciplina.codigo = novo_codigo

                print("Disciplina editada com sucesso!")
                return
        print("Disciplina não encontrada.")

    def editar_sala_de_aula(self, numero_sala):
        for sala in self.salas_de_aula:
            if sala.numero == numero_sala:
                novo_numero = input("Novo número da sala de aula: ")
                nova_capacidade = int(input("Nova capacidade da sala de aula: "))

                sala.numero = novo_numero
                sala.capacidade = nova_capacidade

                print("Sala de aula editada com sucesso!")
                return
        print("Sala de aula não encontrada.")
    
    def editar_grade_aula(self, aluno_nome):
        for aluno in self.alunos:
            if aluno.nome == aluno_nome:
                print("\nDisciplinas disponíveis:")
                for disciplina in self.consultar_disciplinas():
                    print(disciplina.nome)
                nova_disciplina_nome = input("Nova disciplina para o aluno: ")
                print("\nSalas de aula disponíveis:")
                for sala in self.consultar_salas_de_aula():
                    print("Sala:", sala.numero, "Capacidade:", sala.capacidade)
                nova_sala_nome = input("Nova sala de aula para o aluno: ")
                print("\nProfessores disponíveis:")
                for professor in self.consultar_professores():
                    print(f"Professor: {professor.nome}, Idade: {professor.idade}")
                novo_professor_nome = input("Novo professor para o aluno: ")

                disciplina_existente = False
                for disciplina in self.disciplinas:
                    if disciplina.nome == nova_disciplina_nome:
                        disciplina_existente = True
                        break

                sala_existente = False
                for sala in self.salas_de_aula:
                    if sala.numero == nova_sala_nome:
                        sala_existente = True
                        break

                
                professor_existente = False
                for professor in self.professores:
                    if professor.nome == novo_professor_nome:
                        professor_existente = True
                        break

                if disciplina_existente and sala_existente and professor_existente:
                    aluno.associacoes = []
                    disciplina = next((d for d in self.disciplinas if d.nome == nova_disciplina_nome), None)
                    professor = next((p for p in self.professores if p.nome == novo_professor_nome), None)
                    sala = next((s for s in self.salas_de_aula if s.numero == nova_sala_nome), None)
                    aluno.adicionar_associacao(disciplina, professor, sala)
                    print("Grade de aula editada com sucesso!")
                    return
                else:
                    print("Disciplina, sala de aula ou professor não encontrados.")
                    return
        print("Aluno não encontrado.")