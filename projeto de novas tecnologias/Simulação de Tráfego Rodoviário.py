import random
import time
import threading

class Veiculo:
    def __init__(self, tipo, velocidade_maxima):
        self.tipo = tipo
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0
        self.posicao = 0

    def acelerar(self):
        aceleracao = random.uniform(1, 5)
        self.velocidade_atual += aceleracao
        if self.velocidade_atual > self.velocidade_maxima:
            self.velocidade_atual = self.velocidade_maxima

    def desacelerar(self):
        desaceleracao = random.uniform(1, 3)
        self.velocidade_atual -= desaceleracao
        if self.velocidade_atual < 0:
            self.velocidade_atual = 0

    def mudar_faixa(self):
        print(f"{self.tipo} mudando de faixa.")
    
    def mover(self):
        self.posicao += self.velocidade_atual

class Carro(Veiculo):
    def __init__(self):
        super().__init__('Carro', 180)

class Caminhao(Veiculo):
    def __init__(self):
        super().__init__('Caminhão', 100)

class Onibus(Veiculo):
    def __init__(self):
        super().__init__('Ônibus', 120)

class Moto(Veiculo):
    def __init__(self):
        super().__init__('Moto', 200)

def simular_veiculos(veiculos, parar):
    while not parar.is_set():
        for veiculo in veiculos:
            veiculo.acelerar()
            veiculo.mover()
            print(f"{veiculo.tipo}: Velocidade: {veiculo.velocidade_atual} km/h, Posição: {veiculo.posicao} km")
            time.sleep(1)

            # Verificar se o veículo deve mudar de faixa (50% de chance a cada passo de tempo)
            if isinstance(veiculo, Moto) and random.random() < 0.5:
                veiculo.mudar_faixa()

def simular_trafego():
    veiculos = [Carro(), Caminhao(), Onibus(), Moto()]
    parar_simulacao = threading.Event()
    simulacao_thread = threading.Thread(target=simular_veiculos, args=(veiculos, parar_simulacao))
    simulacao_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulação encerrada.")
        parar_simulacao.set()
        simulacao_thread.join()

simular_trafego()

