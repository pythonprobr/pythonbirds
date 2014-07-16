# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest.case import TestCase
import placa_grafica


class TestesDoMotor(TestCase):
    def teste_inverter_coordenadas(self):
        self.assertTupleEqual((0, placa_grafica.ALTURA-1), placa_grafica.normalizar_coordenadas(0, 0))
        self.assertTupleEqual((3, placa_grafica.ALTURA - 2), placa_grafica.normalizar_coordenadas(3, 1))
        self.assertTupleEqual((10, 0), placa_grafica.normalizar_coordenadas(10, placa_grafica.ALTURA-1))

    def teste_desenhar_frame_vazio(self):
        self.maxDiff=None
        class PontoCartesiano():
            def __init__(self, x, y, caracter):
                self.caracter = caracter
                self(x,y)

            def __call__(self, x,y):
                self.y = y
                self.x = x


        self.assertEqual(FRAMES[0], placa_grafica.desenhar())
        pontoA = PontoCartesiano(1, 1, 'A')
        self.assertEqual(FRAMES[1], placa_grafica.desenhar(pontoA))
        pontoA.x=2
        self.assertEqual(FRAMES[2], placa_grafica.desenhar(pontoA))
        pontoB=PontoCartesiano(1,1,'B')
        pontoA.y=2
        self.assertEqual(FRAMES[3], placa_grafica.desenhar(pontoA,pontoB))
        pontoB(2,2)
        self.assertEqual(FRAMES[4], placa_grafica.desenhar(pontoA,pontoB))
        pontoB(placa_grafica.LARGURA-1,placa_grafica.ALTURA-1)
        self.assertEqual(FRAMES[4], placa_grafica.desenhar(pontoA,pontoB))


FRAMES =['''|------------------------------------------------------------------------------|
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT|
''',

'''|------------------------------------------------------------------------------|
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|A                                                                             |
|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT|
'''
,

'''|------------------------------------------------------------------------------|
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
| A                                                                            |
|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT|
'''
,

'''|------------------------------------------------------------------------------|
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
| A                                                                            |
|B                                                                             |
|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT|
''',

'''|------------------------------------------------------------------------------|
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
| A                                                                            |
|                                                                              |
|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT|
''',

'''|------------------------------------------------------------------------------|
|                                                                             B|
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT|
''']




















