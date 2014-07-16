# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest.case import TestCase
from atores import Ator, DESTRUIDO, ATIVO


class AtorTestes(TestCase):
    def teste_ator_posicao(self):
        ator = Ator()
        self.assertTupleEqual((0, 0, 'A'), ator.calcular_posicao(0))
        ator = Ator(0.3, 0.5)
        self.assertTupleEqual((0, 0, 'A'), ator.calcular_posicao(2.3))
        ator = Ator(0.6, 2.1)
        self.assertTupleEqual((1, 2, 'A'), ator.calcular_posicao(3.14))

    def test_status(self):
        ator = Ator()
        self.assertEqual(ATIVO, ator.status)
        self.assertEqual('A', ator.calcular_posicao(0)[2])
        ator.status = DESTRUIDO
        self.assertEqual('✝', ator.calcular_posicao(0)[2])
        self.assertEqual(ATIVO, Ator().status)
