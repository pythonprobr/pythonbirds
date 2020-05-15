

from oo.motor import Motor
from oo.direcao import Direcao

class Carro:

    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao
    
    def calcular_velocidade(self):
        return self.motor.velocidade
    
    def calcular_acelerar(self):
        return self.motor.acelerar()

    def calcular_direcao(self):
        return self.direcao.valor
    
    def girar_a_direita(self):
        return self.direcao.direita()
    
    def girar_a_esquerda(self):
        return self.direcao.esquerda()


if __name__ == '__main__':
    carro = Carro(Motor(), Direcao())
    print('Testando o Motor')
    print(carro.calcular_velocidade)
    print('Testando a Direção')
    print(carro.calcular_direcao())
    print(carro.girar_a_direita())
    print(carro.girar_a_esquerda())