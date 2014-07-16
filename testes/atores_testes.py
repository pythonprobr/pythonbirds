# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest.case import TestCase
from atores import Ator


class AtorTestes(TestCase):
    def teste_ator_posicao(self):
        ator = Ator(0, 0)
        self.assertTupleEqual((0, 0, 'A'), ator.calcular_posicao(0))
        ator = Ator(0.3, 0.5)
        self.assertTupleEqual((0, 0, 'A'), ator.calcular_posicao(2.3))
        ator = Ator(0.6, 2.1)
        self.assertTupleEqual((1, 2, 'A'), ator.calcular_posicao(3.14))

