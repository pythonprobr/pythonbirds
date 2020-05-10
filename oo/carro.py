# -*- coding: utf-8 -*-

''' 
Exemplo:
>>> # Testando motor  ##########################################################
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao #######################################################

    >>> direcao = Direcao()
    >>> direcao.valor
    'N'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'L'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'S'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'O'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'N'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'O'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'S'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'L'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'N'

    #Testando Carro #################################################################
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'N'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'L'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'N'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'O'
'''

class Direcao:
    def __init__(self, direcao = "N"):
        self.valor = direcao

    def girar_a_direita(self):
        if self.valor == "N":
            self.valor = "L"
        elif self.valor == "L":
            self.valor = "S"
        elif self.valor == "S":
            self.valor = "O"
        else:
            self.valor = "N"

    def girar_a_esquerda(self):
        if self.valor == "N":
            self.valor = "O"
        elif self.valor == "O":
            self.valor = "S"
        elif self.valor == "S":
            self.valor = "L"
        else:
            self.valor = "N"


class Motor:
    def __init__(self, velocidade = 0, velocidade_max = 180):
        self.velocidade_max = velocidade_max
        self.velocidade = velocidade

    def acelerar(self):
        if self.velocidade < self.velocidade_max:
            self.velocidade += 1
          
    def frear(self):
        if self.velocidade > 1:
            self.velocidade -= 2
        else:
            self.velocidade = 0

class Carro:
    
    def __init__(self, direcao = Direcao(), motor = Motor()):
        self.direcao = direcao
        self.motor = motor

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
    
    

