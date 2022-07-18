# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
import platform
from unittest.case import TestCase
import placa_grafica
from templates import FRAMES


class TestesDoMotor(TestCase):
    def teste_inverter_coordenadas(self):
        self.assertTupleEqual((0, placa_grafica.ALTURA - 1), placa_grafica.normalizar_coordenadas(0, 0))
        self.assertTupleEqual((3, placa_grafica.ALTURA - 2), placa_grafica.normalizar_coordenadas(3, 1))
        self.assertTupleEqual((10, 0), placa_grafica.normalizar_coordenadas(10, placa_grafica.ALTURA - 1))

    def teste_desenhar_frame_vazio(self):
        class PontoCartesiano():
            def __init__(self, x, y, caracter):
                self.caracter = caracter
                self(x, y)

            def __call__(self, x, y):
                self.y = y
                self.x = x

        frames = FRAMES
        if platform.system() == 'Windows':
            frames = [f.replace('\n', os.linesep) for f in frames]

        self.assertEqual(frames[0], placa_grafica.desenhar())
        ponto_a = PontoCartesiano(1, 1, 'A')
        self.assertEqual(frames[1], placa_grafica.desenhar(ponto_a))
        ponto_a.x = 2
        self.assertEqual(frames[2], placa_grafica.desenhar(ponto_a))
        ponto_b = PontoCartesiano(1, 1, 'B')
        ponto_a.y = 2
        self.assertEqual(frames[3], placa_grafica.desenhar(ponto_a, ponto_b))
        ponto_b(2, 2)
        self.assertEqual(frames[4], placa_grafica.desenhar(ponto_a, ponto_b))
        ponto_b(placa_grafica.LARGURA - 1, placa_grafica.ALTURA - 1)
        self.assertEqual(frames[4], placa_grafica.desenhar(ponto_a, ponto_b))
