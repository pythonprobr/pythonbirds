"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades


A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda

       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> carro = Carro()
    >>> carro.motor.acelerar()
    1
    >>> carro.motor.acelerar()
    2
    >>> carro.motor.acelerar()
    3
    >>> carro.motor.frear()
    1
    >>> carro.motor.frear()
    0
    >>> # Testando Direcao
    >>> carro.direcao.girar_a_direita()
    'LESTE'
    >>> carro.direcao.girar_a_direita()
    'SUL'
    >>> carro.direcao.girar_a_direita()
    'OESTE'
    >>> carro.direcao.girar_a_direita()
    'NORTE'
    >>> carro.direcao.girar_a_esquerda()
    'OESTE'
    >>> carro.direcao.girar_a_esquerda()
    'SUL'
    >>> carro.direcao.girar_a_esquerda()
    'LESTE'
    >>> carro.direcao.girar_a_esquerda()
    'NORTE'
    >>> carro.motor.acelerar()
    1
    >>> carro.motor.acelerar()
    2
    >>> carro.motor.frear()
    0
    >>> carro.direcao.girar_a_direita()
    'LESTE'
    >>> carro.direcao.girar_a_esquerda()
    'NORTE'
    >>> carro.direcao.girar_a_esquerda()
    'OESTE'

"""


class Carro:
    def __init__(self):
        self.direcao = Direcao()
        self.motor = Motor()


class Direcao:
    def __init__(self, direcao='NORTE'):
        self.direcao = direcao

    def girar_a_direita(self):
        if self.direcao == 'OESTE':
            self.direcao = 'NORTE'
        elif self.direcao == 'NORTE':
            self.direcao = 'LESTE'
        elif self.direcao == 'SUL':
            self.direcao = 'OESTE'
        else:
            self.direcao = 'SUL'
        return self.direcao

    def girar_a_esquerda(self):
        if self.direcao == 'OESTE':
            self.direcao = 'SUL'
        elif self.direcao == 'NORTE':
            self.direcao = 'OESTE'
        elif self.direcao == 'SUL':
            self.direcao = 'LESTE'
        else:
            self.direcao = 'NORTE'
        return self.direcao


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def __str__(self):
        return f'Velocidade {self.velocidade}'

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        if self.velocidade == 1 or self.velocidade == 0:
            self.velocidade = 0
        else:
            self.velocidade -= 2
        return self.velocidade


if __name__ == '__main__':
    carro = Carro()
    print(carro.motor.acelerar())
    print(carro.motor.acelerar())
    print(carro.motor.frear())
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_esquerda())
