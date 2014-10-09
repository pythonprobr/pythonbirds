# -*- coding: utf-8 -*-
from os import path
import sys

project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)

from atores import PassaroAmarelo, PassaroVermelho, Obstaculo, Porco
from fase import Fase
from placa_grafica_tkinter import rodar_fase

if __name__ == '__main__':
    fase = Fase(intervalo_de_colisao=32)


    # Adicionar Pássaros Vermelhos
    for i in range(5):
        fase.adicionar_passaro(PassaroVermelho(30, 30))
    # Adicionar Pássaros Amarelos
    for i in range(30):
        fase.adicionar_passaro(PassaroAmarelo(30, 30))


    # Obstaculos
    for i in range(30, 480, 32):
        fase.adicionar_obstaculo(Obstaculo(300, i))

    # Porcos
    for i in range(30, 300, 32):
        fase.adicionar_porco(Porco(600, i))

    rodar_fase(fase)