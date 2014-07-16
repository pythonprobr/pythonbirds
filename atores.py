# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Ator():
    caracter = 'A'

    def __init__(self, x, y):
        self.y = y
        self.x = x

    def calcular_posicao(self, tempo):
        return round(self.x), round(self.y), self.caracter


