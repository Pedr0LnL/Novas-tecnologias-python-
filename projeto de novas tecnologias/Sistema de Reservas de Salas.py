import datetime
import pickle

class Sala:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.reservas = {}

    def adicionar_reserva(self, reserva):
        if reserva.data_hora_inicio not in self.reservas:
            self.reservas[reserva.data_hora_inicio] = reserva
            print("Reserva adicionada com sucesso.")
        else:
            print("Esta sala já está reservada neste horário.")

    def cancelar_reserva(self, data_hora_inicio):
        if data_hora_inicio in self.reservas:
            del self.reservas[data_hora_inicio]
            print("Reserva cancelada com sucesso.")
        else:
            print("Não há reserva nesta sala neste horário.")

    def verificar_disponibilidade(self, data_hora_inicio, duracao):
        horario_fim = data_hora_inicio + datetime.timedelta(minutes=duracao)
        for reserva in self.reservas.values():
            if (data_hora_inicio >= reserva.data_hora_inicio and data_hora_inicio < reserva.data_hora_fim) or \
               (horario_fim > reserva.data_hora_inicio and horario_fim <= reserva.data_hora_fim):
                return False
        return True

    def __str__(self):
        return f"Sala: {self.nome}, Capacidade: {self.capacidade}"

class Reserva:
    def __init__(self, sala, data_hora_inicio, duracao, responsavel):
        self.sala = sala
        self.data_hora_inicio = data_hora_inicio
        self.duracao = duracao
        self.data_hora_fim = data_hora_inicio + datetime.timedelta(minutes=duracao)
        self.responsavel = responsavel

    def __str__(self):
        return f"Reserva para a sala {self.sala.nome}, Início: {self.data_hora_inicio}, Duração: {self.duracao} minutos, Responsável: {self.responsavel}"

class GerenciadorSalas:
    def __init__(self):
        self.salas = {}

    def adicionar_sala(self, sala):
        self.salas[sala.nome] = sala
        print("Sala adicionada com sucesso.")

    def listar_salas(self):
        for sala in self.salas.values():
            print(sala)

    def salvar_salas(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.salas, f)

    def carregar_salas(self, filename):
        with open(filename, 'rb') as f:
            self.salas = pickle.load(f)

def menu_principal():
    print("Bem-vindo ao sistema de gerenciamento de reservas de salas de reunião.")
    print("1. Visualizar disponibilidade das salas")
    print("2. Fazer uma reserva")
    print("3. Cancelar uma reserva")
    print("4. Sair")

def fazer_reserva(gerenciador):
    print("Fazer uma reserva")
    gerenciador.listar_salas()
    sala_nome = input("Selecione o nome da sala: ")
    if sala_nome not in gerenciador.salas:
        print("Sala não encontrada.")
        return
    data_str = input("Digite a data e hora de início (formato: YYYY-MM-DD HH:MM): ")
    data_hora_inicio = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
    duracao = int(input("Digite a duração da reserva em minutos: "))
    responsavel = input("Digite o nome do responsável pela reserva: ")
    sala = gerenciador.salas[sala_nome]
    if sala.verificar_disponibilidade(data_hora_inicio, duracao):
        reserva = Reserva(sala, data_hora_inicio, duracao, responsavel)
        sala.adicionar_reserva(reserva)
    else:
        print("A sala não está disponível neste horário.")

def cancelar_reserva(gerenciador):
    print("Cancelar uma reserva")
    sala_nome = input("Selecione o nome da sala: ")
    if sala_nome not in gerenciador.salas:
        print("Sala não encontrada.")
        return
    data_str = input("Digite a data e hora de início da reserva a ser cancelada (formato: YYYY-MM-DD HH:MM): ")
    data_hora_inicio = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M")
    sala = gerenciador.salas[sala_nome]
    sala.cancelar_reserva(data_hora_inicio)

if __name__ == "__main__":
    gerenciador = GerenciadorSalas()
    gerenciador.adicionar_sala(Sala("Sala 1", 10))
    gerenciador.adicionar_sala(Sala("Sala 2", 8))
    gerenciador.adicionar_sala(Sala("Sala 3", 12))

    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerenciador.listar_salas()
        elif opcao == "2":
            fazer_reserva(gerenciador)
        elif opcao == "3":
            cancelar_reserva(gerenciador)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
