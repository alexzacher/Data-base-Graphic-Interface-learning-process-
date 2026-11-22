from abc import ABC, abstractmethod
from rich import print, inspect
import random
from rich.table import Table

class Personagem (ABC):
    def __init__(self, nome, vida = 100 ):
        #--- atibutos
        self.nome = nome
        self.vida = vida
        self.golpe = []


    #--- Metodos
    def atacar (self, alvo, dano = 50): #ataque aleatorio nao passa de 100 ( randint )
        if self.vida > 0 and alvo.vida > 0:
            fator = alvo.receber_dano(dano)
            #alvo.vida = alvo.vida - fator
            table = Table(title="Jogo")
            table.add_column('Atacante')
            table.add_column('Defensor')
            table.add_column('Tipo de ataque')
            table.add_column('Dano dado')
            table.add_column('Dano sofrido')
            table.add_column('Vida')
            #print(f'Dado dado {dano}, dado recebido {fator}, vida total {alvo.vida}, {self.nome} {alvo.nome}')
            x = random.choice(self.golpe)
            table.add_row( self.nome, alvo.nome, x, str(dano), str(fator),str(alvo.vida))
            print(table)

        if self.vida or alvo.vida == 0:
            if self.vida <= 0:
                print(f'{self.nome} ja esta morto')
            elif alvo.vida <= 0:
                print(f'{alvo.nome} ja esta morto - Nao podera efeturar mais atagues no/a {alvo.nome}.')

    def receber_dano (self, dano): # Encapsular
        fator = random.randint(1, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        return fator
        #print(f'O personagem {self.nome} recebeu {fator} de dado, e esta com {self.vida}')

    @abstractmethod
    def curar(self):
        pass

# ------------- SubClass 1 ------------------
class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        #--- atibutos
        self.golpe = ['Espada', 'Uso de escudo', 'Corpo a corpo']

    #--- Metodos
    def curar(self, cura = 5):
        fator_cura = random.randint(1, cura)
        if self.vida + fator_cura < 100:
            self.vida += fator_cura
            print(f'>>> Vc curou {fator_cura} do/a {type(self).__name__}, tenho o total de {self.vida} vida')
        elif self.vida + fator_cura > 100:
            self.vida = 100
            print(f'>>> Vc curou {fator_cura} do/a {type(self).__name__}, tenho o total de {self.vida} vida')


# ------------- SubClass 2 ------------------
class Mago(Personagem):
    def __init__(self, nome, vida = 100):
        super().__init__(nome, vida)
        #vida = self.receber_dano
    #--- atibutos
        self.golpe = ['Bola de jogo', 'Magia de dado', 'Congelar']

    #--- Metodos
    def curar(self, cura = 5):
        fator_cura = random.randint(1, cura)
        if self.vida > 0:
            if self.vida + fator_cura < 120:
                self.vida += fator_cura
                print(f'>>> Vc curou {fator_cura} do/a {type(self).__name__}, tenho o total de {self.vida} vida')
            elif self.vida + fator_cura > 120:
                self.vida = 100
                print(f'>>> Vc curou {fator_cura} do/a {type(self).__name__}, tenho o total de {self.vida} vida')
        else:
            print(f'{self.nome} nao podera se curar pois esta morto.')

# ---------------------------------------------
# ---------------------------------------------
g = Guerreiro("Gurreiro", 100)
m = Mago("Mago", 100)


g.atacar(m, 100000)
m.curar(100)

m.atacar(g, 100)
g.curar(100)
inspect(g, methods=True)
inspect(m, methods=True)
