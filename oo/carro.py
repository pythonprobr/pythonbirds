# -*- coding: utf-8 -*-

''' 
Exemplo:
    #testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.velocidade_max
    180
    
'''



class Direcao:
    def __init__(self, direcao = "N"):
        self.direcao = direcao

    def virar_a_direita(self):
        if self.direcao == "N":
            self.direcao = "L"
        elif self.direcao == "L":
            self.direcao = "S"
        elif self.direcao == "S":
            self.direcao = "O"
        else:
            self.direcao = "N"
        return self.direcao

    def virar_a_esquerda(self):
        if self.direcao == "N":
            self.direcao = "O"
        elif self.direcao == "O":
            self.direcao = "S"
        elif self.direcao == "S":
            self.direcao = "L"
        else:
            self.direcao = "N"
        return self.direcao


class Motor:
    def __init__(self, velocidade = 0, velocidade_max = 180):
        self.velocidade_max = velocidade_max
        self.velocidade = velocidade

    def acelerar(self):
        if self.velocidade < self.velocidade_max:
            self.velocidade += 1
            return f"A velocidade atual foi aumentada para: {self.velocidade}"
        else:
            return "Velocidade atual é a máxima"
        
    def desacelerar(self):
        if self.velocidade > 1:
            self.velocidade -= 2
            return "O carro desacelerou para: {}".format(self.velocidade)
        else:
            self.velocidade = 0
            return self.velocidade

class Carro:
    
    def __init__(self, direcao = Direcao(), motor = Motor()):
        self.direcao = direcao
        self.motor = motor

if __name__ == "__main__":
    import doctest
    doctest.testmod()