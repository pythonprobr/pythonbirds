# -*- coding: utf-8 -*-
from os import path
import sys
import math

project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)

from atores import PassaroAmarelo, PassaroVermelho, Obstaculo, Porco
from fase import Fase
from placa_grafica_tkinter import rodar_fase
from random import randint

if __name__ == '__main__':
    fase = Fase(intervalo_de_colisao=32)


    # Adicionar Pássaros Amarelos
    for i in range(80):
        fase.adicionar_passaro(PassaroAmarelo(30, 30))


    # Obstaculos
    theta = 270
    h = 12
    k = 7
    step = 32
    r = 50

    while theta < 480:
        x = 600 + (h + r * math.cos(theta))
        y = (k + r * math.sin(theta))
        fase.adicionar_obstaculo(Obstaculo(x, y))
        theta += 32

    # Porcos
    for i in range(30, 300, 32):
        x = randint(590, 631)
        y = randint(0, 21)
        fase.adicionar_porco(Porco(x, y))

    rodar_fase(fase)