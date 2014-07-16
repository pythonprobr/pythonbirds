# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest.case import TestCase
from atores import Ator, DESTRUIDO, ATIVO, Obstaculo


def assert_ator_status(test_case, ator, caracter_status_ativo, carater_status_destruido):
    test_case.assertEqual(ATIVO, ator.status(0))
    test_case.assertEqual(caracter_status_ativo, ator.caracter(0))
    ator.colidir(ator, 3.2)
    test_case.assertEqual(ATIVO, ator.status(3.1))
    test_case.assertEqual(caracter_status_ativo, ator.caracter(3.1))
    test_case.assertEqual(DESTRUIDO, ator.status(3.2))
    test_case.assertEqual(carater_status_destruido, ator.caracter(3.2))
    test_case.assertEqual(DESTRUIDO, ator.status(4))
    test_case.assertEqual(carater_status_destruido, ator.caracter(4))


class AtorTestes(TestCase):
    def teste_ator_posicao(self):
        ator = Ator()
        self.assertTupleEqual((0, 0), ator.calcular_posicao(0))
        ator = Ator(0.3, 0.5)
        self.assertTupleEqual((0, 0), ator.calcular_posicao(2.3))
        ator = Ator(0.6, 2.1)
        self.assertTupleEqual((1, 2), ator.calcular_posicao(3.14))

    def assert_colisao_atores_ativos(self, ator, ator2):
        tempo_da_colisao = 2
        self.assertEqual(ator.status(tempo_da_colisao), ATIVO)
        self.assertEqual(ator2.status(tempo_da_colisao), ATIVO)
        ator.colidir(ator2, tempo_da_colisao)
        self.assertEqual(ator2.status(tempo_da_colisao), DESTRUIDO)
        self.assertEqual(ator.status(tempo_da_colisao), DESTRUIDO)

    def assert_nao_colisao(self, ator, ator2):
        tempo_da_colisao = 2
        status_iniciais = [ator.status(tempo_da_colisao), ator2.status(tempo_da_colisao)]
        ator.colidir(ator2, tempo_da_colisao)
        self.assertListEqual(status_iniciais, [ator.status(tempo_da_colisao), ator2.status(tempo_da_colisao)])

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

    def teste_nao_colisao_entre_atores_ativos(self):
        self.assert_nao_colisao(Ator(2, 2), Ator(2, 4))
        self.assert_nao_colisao(Ator(2, 2), Ator(3, 4))
        self.assert_nao_colisao(Ator(2, 2), Ator(4, 2))
        self.assert_nao_colisao(Ator(2, 2), Ator(3, 0))
        self.assert_nao_colisao(Ator(2, 2), Ator(2, 0))
        self.assert_nao_colisao(Ator(2, 2), Ator(0, 1))
        self.assert_nao_colisao(Ator(2, 2), Ator(0, 2))
        self.assert_nao_colisao(Ator(2, 2), Ator(0, 4))

    def teste_colisao_somente_um_ator_destruido(self):
        ator = Ator(2, 2)
        ator.colidir(ator,0)
        ator2 = Ator(2, 2)
        self.assert_nao_colisao(ator, ator2)
        self.assert_nao_colisao(Ator(2, 3), ator)
        self.assert_nao_colisao(Ator(3, 3), ator)
        self.assert_nao_colisao(Ator(3, 2), ator)
        self.assert_nao_colisao(Ator(3, 1), ator)
        self.assert_nao_colisao(Ator(2, 1), ator)
        self.assert_nao_colisao(Ator(1, 1), ator)
        self.assert_nao_colisao(Ator(1, 2), ator)
        self.assert_nao_colisao(Ator(1, 3), ator)
        self.assert_nao_colisao(ator2, ator)
        self.assert_nao_colisao(Ator(2, 3), ator)
        self.assert_nao_colisao(Ator(3, 3), ator)
        self.assert_nao_colisao(Ator(3, 2), ator)
        self.assert_nao_colisao(Ator(3, 1), ator)
        self.assert_nao_colisao(Ator(2, 1), ator)
        self.assert_nao_colisao(Ator(1, 1), ator)
        self.assert_nao_colisao(Ator(1, 2), ator)
        self.assert_nao_colisao(Ator(1, 3), ator)

    def teste_status(self):
        ator = Ator()
        assert_ator_status(self, ator, 'A', '✝')


class ObstaculoTestes(TestCase):
    def teste_status(self):
        obstaculo = Obstaculo()
        assert_ator_status(self, obstaculo, 'O', ' ')

class PorcoTestes(TestCase):
    def teste_status(self):
        porco = Porco()
        assert_ator_status(self, porco, '☺', '✝')



