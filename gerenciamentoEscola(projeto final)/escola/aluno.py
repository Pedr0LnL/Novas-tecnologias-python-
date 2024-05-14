class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.associacoes = []

    def adicionar_associacao(self, disciplina, professor, sala_de_aula):
        self.associacoes.append({"disciplina": disciplina, "professor": professor, "sala_de_aula": sala_de_aula})

    def associar_disciplina(self, disciplina):
        self.disciplina = disciplina

    def associar_professor(self, professor):
        self.professor = professor

    def associar_sala_de_aula(self, sala_de_aula):
        self.sala_de_aula = sala_de_aula

    def consultar_associacoes(self):
        return self.associacoes