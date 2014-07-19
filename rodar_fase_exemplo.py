# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from atores import PassaroAmarelo, PassaroVermelho, Obstaculo, Porco
from fase import Fase
from placa_grafica_tkinter import rodar_fase

fase = Fase(intervalo_de_colisao=10)


# Adicion Pássaros Vermelhos
for i in range(5):
    fase.adicionar_passaro(PassaroVermelho(30, 30))
# Adicion Pássaros Amarelos
for i in range(30):
    fase.adicionar_passaro(PassaroAmarelo(30, 30))


#Obstaculos
for i in range(30, 480, 32):
    fase.adicionar_obstaculo(Obstaculo(300, i))

# Porcos
for i in range(30, 300,32):
    fase.adicionar_porco(Porco(600, i))




rodar_fase(fase)