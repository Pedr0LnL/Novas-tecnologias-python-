from escola.disciplina import Disciplina

class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade

    def remover_disciplina(self, codigo_disciplina):
        for disciplina in self.disciplinas:
            if disciplina.codigo == codigo_disciplina:
                self.disciplinas.remove(disciplina)
                return True
        return False

    def atualizar_info(self, novo_nome, nova_idade):
        self.nome = novo_nome
        self.idade = nova_idade

    def consultar_disciplinas(self):
        return self.disciplinas