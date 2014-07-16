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

    def calcular_posicao(self, tempo):
        caracter = self.caracter if self.status == ATIVO else '✝'
        return round(self.x), round(self.y), caracter


