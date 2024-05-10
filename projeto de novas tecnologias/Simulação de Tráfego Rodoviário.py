import random
import time

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
        pass

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

def simular_trafego():
    veiculos = [Carro(), Caminhao(), Onibus()]

    while True:
        for veiculo in veiculos:
            veiculo.acelerar()
            veiculo.mover()
            print(f"{veiculo.tipo}: Velocidade: {veiculo.velocidade_atual} km/h, Posição: {veiculo.posicao} km")
            time.sleep(1)

simular_trafego()
