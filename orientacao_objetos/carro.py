"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por duas classes:
1- Motor 2- Direção

1-Motor
O motor terá a responsabilidade de controlar a velocidade do carro.
Ele oferece os seguintes atributos:
A- Atributo de dado velocidade;
B- Método acelerar: deverá incrementar a velocidade de 1 unidade
C- Método frear: deverá diminuir a velocidade de 2 unidades

2-Direção
A direção terá a responsabilidade de contralar a direção.
Ela oferece os seguintes atributos:
A- Valores de direção: norte, sul, leste e oeste.
B- Método 1: girar a direita
C- Método 2: girar a esquerda
Agora, para se emular esses comportamentos é necessário fazer a escrita do código em forma de uma documentação.

Exemplo

    >>> #testando motor
    >>> motor = Motor( )
    >>> motor.velocidade
    0
    >>> motor.acelerar( )
    >>> motor.velocidade
    1
    >>> motor.acelerar( )
    >>> motor.velocidade
    2
    >>> motor.acelerar( )
    >>> motor.velocidade
    3
    >>> motor.frear( )
    >>> motor.velocidade
    1
    >>> motor.frear( )
    >>> motor.velocidade
    0
    >>> #testando Direção
    >>> direcao = Direcao( )
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> #aqui a classe carro delega as lógicas acima para os objetos(direção e motor)
    >>> #através de composição(ajuntar todos delegando o q cada um faz)

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade( )
    0
    >>> carro.acelerar( )
    >>> carro.calcular_velocidade( )
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade( )
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade( )
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Direcao:
    #O PROFESSOR DECIDIU USAR UM DICIONARIO!!
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}

    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()







