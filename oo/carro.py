class Motor:
    # Responsabilidade de controlar a velocidade
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
       self.velocidade += 1
       return self.velocidade

    def frear(self):
       self.velocidade -= 2
       if self.velocidade < 0:
           self.velocidade = 0
       return self.velocidade

class Direcao:
    # Responsabilidade de controlar a direção
    def __init__(self):
        self.valor = 'Norte'
        self.posicao = 0
        self.direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']


    def mostra_direcao(self):
        return self.direcoes[self.posicao]
    
    def direita(self):
        self.posicao += 1
        if self.posicao <= 3:
            self.valor = self.direcoes[self.posicao]
        else:
            self.posicao = 0
            self.valor = self.direcoes[self.posicao]

        return self.valor

    def esquerda(self):
        self.posicao -= 1
        if self.posicao >= 0:
            self.valor = self.direcoes[self.posicao]
        else:
            self.posicao = len(self.direcoes) - 1
            self.valor = self.direcoes[self.posicao]

        return self.valor

class Carro:

    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao
    
    def calcular_velocidade(self):
        return self.motor.velocidade
    
    def acelerar(self):
        return self.motor.acelerar()
    
    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor
    
    def girar_a_direita(self):
        return self.direcao.direita()
    
    def girar_a_esquerda(self):
        return self.direcao.esquerda()


if __name__ == '__main__':
    direcao = Direcao()
    motor = Motor()
    carro = Carro(direcao, motor)
    print('Testando o Motor')
    print(carro.calcular_velocidade())
    print(carro.acelerar())
    print(carro.acelerar())
    print(carro.acelerar())
    print(carro.frear())
    print('Testando a Direção')
    print(carro.calcular_direcao())
    print(carro.girar_a_direita())
    print(carro.girar_a_direita())
    print(carro.girar_a_esquerda())
    print(carro.girar_a_direita())
    print(carro.girar_a_direita())
    print(carro.girar_a_direita())
    print(carro.girar_a_esquerda())
    print(carro.girar_a_esquerda())
    print(carro.girar_a_esquerda())
