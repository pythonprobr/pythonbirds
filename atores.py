# -*- coding: utf-8 -*-

from __future__ import unicode_literals

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'


class Ator():
    caracter = 'A'

    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x
        self.status = ATIVO

    def ponto_cartesiano_inteiro(self):
        return round(self.x), round(self.y)

    def calcular_posicao(self, tempo):
        caracter = self.caracter if self.status == ATIVO else '✝'
        x, y = self.ponto_cartesiano_inteiro()
        return x, y, caracter

    def colidir(self, outro_ator):
        if self.status == DESTRUIDO or outro_ator.status == DESTRUIDO:
            return False
        x1, y1 = self.ponto_cartesiano_inteiro()
        x2, y2 = outro_ator.ponto_cartesiano_inteiro()

        def esta_no_intervalo(coordenada1, coordenada2, intervalo=1):
            coordenadas = sorted([coordenada1, coordenada2])
            return coordenadas[1] - intervalo <= coordenadas[0]

        if esta_no_intervalo(x1, x2) and esta_no_intervalo(y1, y2):
            self.status = DESTRUIDO
            outro_ator.status = DESTRUIDO
            return True
        return False

class Obstaculo(Ator):
    pass


