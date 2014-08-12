# -*- coding: utf-8 -*-
from atores import ATIVO


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)

