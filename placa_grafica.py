# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
import time
FIM='''|------------------------------------------------------------------------------|
|                                                                              |
|                                                                              |
|                   PPPP  Y   Y  TTTTT H   H  OOO  NN   N                      |
|                   P   P  Y Y     T   H   H O   O N N  N                      |
|                   PPPP    Y      T   HHHHH O   O N  N N                      |
|                   P       Y      T   H   H O   O N   NN                      |
|                   P       Y      T   H   H  OOO  N    N                      |
|                                                                              |
|                                                                              |
|                                                                              |
|                       BBBB    I   RRRR  DDDD   SSSS                          |
|                       B   B   I   R   R D   D S                              |
|                       BBBB    I   RRRR  D   D  SSS                           |
|                       B   B   I   R R   D   D     S                          |
|                       BBBB    I   R   R DDDD  SSSS                           |
|                                                                              |
|                                                                              |
|                                                                              |
|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT|
'''

LARGURA = 80
ALTURA = 20


def apagar_tela():
    os.system('clear')


try:
    apagar_tela()
except:
    apagar_tela = lambda: os.system('cls')


def animar(fase, passo=0.1, delta_t=0.1):
    tempo = 0
    while not fase.acabou(tempo):
        time.sleep(passo)
        apagar_tela()
        pontos_cartesianos = fase.calcular_pontos(tempo)
        print(desenhar(*pontos_cartesianos))
        tempo += delta_t
    print(FIM)
    print(fase.status())


def normalizar_coordenadas(x, y):
    return x, ALTURA - y - 1


def esta_dentro_da_tela(x, y):
    return 0 < x < (LARGURA - 1) and 0 < y < (ALTURA - 1)


def escolher_caracter_limitrofe(x, y):
    if x == 0 or x == LARGURA - 1:
        return '|'
    if y == 0:
        return '-'
    return 'T'


def escolher_caracter(x, y, *pontos_cartesianos):
    for ponto in pontos_cartesianos:
        x_normalizdo, y_normalizado = normalizar_coordenadas(ponto.x, ponto.y)
        if x == x_normalizdo and y == y_normalizado:
            return ponto.caracter
    return ' '


def desenhar(*pontos_cartesianos):
    frame = ''
    for y in range(ALTURA):
        for x in range(LARGURA):
            if esta_dentro_da_tela(x, y):
                frame += escolher_caracter(x, y, *pontos_cartesianos)
            else:
                frame += escolher_caracter_limitrofe(x, y)
        frame += os.linesep
    return frame


def main():
    global Ponto, Fase

    class Ponto():
        def __init__(self, caracter):
            self.caracter = caracter
            self(0)

        def __call__(self, tempo):
            self.y = round(ALTURA * tempo / 5) if tempo < 5 else round(ALTURA * (10 - tempo) / 5)
            self.x = round(LARGURA * tempo / 10)
            return self

    class Fase():
        def __init__(self):
            self.p = Ponto('>')

        def calcular_pontos(self, tempo):
            return [self.p(tempo)]

        def acabou(self, tempo):
            return tempo > 10

        def status(self):
            return 'Você ganhou'

    animar(Fase())


if __name__ == '__main__':
    main()

