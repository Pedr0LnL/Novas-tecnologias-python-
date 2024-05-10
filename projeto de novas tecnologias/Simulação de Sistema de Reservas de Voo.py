class Voo:
    def __init__(self, numero_voo, origem, destino, horario_partida, horario_chegada, assentos_totais):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.horario_partida = horario_partida
        self.horario_chegada = horario_chegada
        self.assentos_totais = assentos_totais
        self.assentos_disponiveis = assentos_totais
        self.assentos = [Assento(i) for i in range(1, assentos_totais + 1)]

    def mostrar_informacoes(self):
        print(f"Número do Voo: {self.numero_voo}")
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")
        print(f"Horário de Partida: {self.horario_partida}")
        print(f"Horário de Chegada: {self.horario_chegada}")
        print(f"Assentos Disponíveis: {self.assentos_disponiveis}/{self.assentos_totais}")

    def encontrar_assentos_disponiveis(self):
        return [assento for assento in self.assentos if not assento.reservado]

    def reservar_assento(self, nome_passageiro, numero_assento):
        for assento in self.assentos:
            if assento.numero_assento == numero_assento and not assento.reservado:
                assento.reservar(nome_passageiro)
                self.assentos_disponiveis -= 1
                return True
        return False

    def cancelar_reserva(self, numero_assento):
        for assento in self.assentos:
            if assento.numero_assento == numero_assento and assento.reservado:
                assento.cancelar_reserva()
                self.assentos_disponiveis += 1
                return True
        return False


class Assento:
    def __init__(self, numero_assento):
        self.numero_assento = numero_assento
        self.reservado = False
        self.nome_passageiro = None

    def reservar(self, nome_passageiro):
        self.reservado = True
        self.nome_passageiro = nome_passageiro

    def cancelar_reserva(self):
        self.reservado = False
        self.nome_passageiro = None


class Passageiro:
    def __init__(self, nome):
        self.nome = nome


class SistemaReservaAerea:
    def __init__(self):
        self.voos = []

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def mostrar_voos_disponiveis(self):
        for voo in self.voos:
            voo.mostrar_informacoes()
            assentos_disponiveis = voo.encontrar_assentos_disponiveis()
            if assentos_disponiveis:
                print("Assentos Disponíveis:")
                for assento in assentos_disponiveis:
                    print(f"Número do Assento: {assento.numero_assento}")
            else:
                print("Não há assentos disponíveis para este voo.")
            print()

    def reservar_assento(self, numero_voo, nome_passageiro, numero_assento):
        for voo in self.voos:
            if voo.numero_voo == numero_voo:
                return voo.reservar_assento(nome_passageiro, numero_assento)
        return False

    def cancelar_reserva(self, numero_voo, numero_assento):
        for voo in self.voos:
            if voo.numero_voo == numero_voo:
                return voo.cancelar_reserva(numero_assento)
        return False

def obter_numero_inteiro(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():  # Verifica se a entrada contém apenas dígitos
            return int(entrada)
        else:
            print("Por favor, insira um número inteiro válido.")

def interface_usuario(sistema_reserva):
    while True:
        print("\nEscolha uma opção:")
        print("1. Mostrar voos disponíveis")
        print("2. Reservar um assento")
        print("3. Cancelar uma reserva")
        print("4. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            sistema_reserva.mostrar_voos_disponiveis()
        elif opcao == "2":
            numero_voo = input("Digite o número do voo: ")
            nome_passageiro = input("Digite o nome do passageiro: ")
            numero_assento = obter_numero_inteiro("Digite o número do assento desejado: ")
            sucesso = sistema_reserva.reservar_assento(numero_voo, nome_passageiro, numero_assento)
            if sucesso:
                print("Assento reservado com sucesso!")
            else:
                print("Não foi possível reservar o assento.")
        elif opcao == "3":
            numero_voo = input("Digite o número do voo: ")
            numero_assento = obter_numero_inteiro("Digite o número do assento a ser cancelado: ")
            sucesso = sistema_reserva.cancelar_reserva(numero_voo, numero_assento)
            if sucesso:
                print("Reserva cancelada com sucesso!")
            else:
                print("Não foi possível cancelar a reserva.")
        elif opcao == "4":
            print("Obrigado por usar o sistema de reserva!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


# Exemplo de Uso:

# Criar sistema de reserva
sistema_reserva = SistemaReservaAerea()

# Adicionar alguns voos
voo1 = Voo("BA123", "Londres", "Nova York", "10:00", "14:00", 100)
voo2 = Voo("AA456", "Nova York", "Los Angeles", "15:00", "18:00", 120)
sistema_reserva.adicionar_voo(voo1)
sistema_reserva.adicionar_voo(voo2)

# Interface com o usuário
interface_usuario(sistema_reserva)
