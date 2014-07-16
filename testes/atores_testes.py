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

    def teste_status(self):
        ator = Ator()
        self.assertEqual(ATIVO, ator.status)
        self.assertEqual('A', ator.calcular_posicao(0)[2])
        ator.status = DESTRUIDO
        self.assertEqual('✝', ator.calcular_posicao(0)[2])
        self.assertEqual(ATIVO, Ator().status)

    def assert_colisao_atores_ativos(self, ator, ator2):
        self.assertEqual(ator.status, ATIVO)
        self.assertEqual(ator2.status, ATIVO)
        self.assertTrue(ator.colidir(ator2))
        self.assertEqual(ator2.status, DESTRUIDO)
        self.assertEqual(ator.status, DESTRUIDO)


    def teste_colisao_entre_atores_ativos(self):
        ator = Ator(2, 2)
        ator2 = Ator(2, 2)
        self.assert_colisao_atores_ativos(ator, ator2)
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(2, 3))
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(3, 3))
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(3, 2))
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(3, 1))
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(2, 1))
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(1, 1))
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(1, 2))
        self.assert_colisao_atores_ativos(Ator(2, 2), Ator(1, 3))


