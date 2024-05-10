import random

class Personagem:
    def __init__(self, nome, classe, vida, ataque, defesa):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        return dano

    def curar(self):
        cura = random.randint(10, 20)
        self.vida = min(100, self.vida + cura)
        return cura

class Inimigo:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        return dano

class Jogo:
    def __init__(self, jogador):
        self.jogador = jogador
        self.inimigos = [Inimigo("Goblin", 20, 6, 2),
                         Inimigo("Esqueleto", 30, 8, 4),
                         Inimigo("Ogro", 50, 12, 6)]
        self.missao_atual = 0

    def batalha(self, inimigo):
        print(f"Você encontrou um {inimigo.nome}!")
        while self.jogador.vida > 0 and inimigo.vida > 0:
            print(f"{self.jogador.nome} ({self.jogador.vida} HP) vs {inimigo.nome} ({inimigo.vida} HP)")
            acao = input("Escolha uma ação: (1) Atacar (2) Curar\n")
            if acao == '1':
                dano_jogador = self.jogador.atacar(inimigo)
                print(f"{self.jogador.nome} causou {dano_jogador} de dano em {inimigo.nome}!")
            elif acao == '2':
                cura = self.jogador.curar()
                print(f"{self.jogador.nome} se curou em {cura} HP.")
            else:
                print("Ação inválida. Tente novamente.")
                continue

            if inimigo.vida <= 0:
                print(f"{inimigo.nome} foi derrotado!")
                break

            dano_inimigo = inimigo.atacar(self.jogador)
            print(f"{inimigo.nome} causou {dano_inimigo} de dano em {self.jogador.nome}!")
            if self.jogador.vida <= 0:
                print(f"{self.jogador.nome} foi derrotado...")
                break

    def explorar(self):
        inimigo = random.choice(self.inimigos)
        self.batalha(inimigo)

    def proxima_missao(self):
        self.missao_atual += 1
        if self.missao_atual < len(self.inimigos):
            print("Você encontrou um novo desafio!")
            self.batalha(self.inimigos[self.missao_atual])
        else:
            print("Você completou todas as missões!")

# Criar um jogador
nome = input("Digite o nome do seu personagem: ")
classe = input("Escolha a classe do seu personagem (Guerreiro, Mago, Arqueiro): ")
jogador = Personagem(nome, classe, 100, 10, 5)

# Iniciar o jogo
jogo = Jogo(jogador)

# Loop principal do jogo
while True:
    opcao = input("Escolha uma ação: (1) Explorar (2) Próxima Missão (3) Sair\n")
    if opcao == '1':
        jogo.explorar()
    elif opcao == '2':
        jogo.proxima_missao()
    elif opcao == '3':
        print("Fim do jogo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
