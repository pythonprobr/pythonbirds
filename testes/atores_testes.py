# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest.case import TestCase
from atores import Ator, DESTRUIDO, ATIVO, Obstaculo


class AtorTestes(TestCase):
    def teste_ator_posicao(self):
        ator = Ator()
        self.assertTupleEqual((0, 0), ator.calcular_posicao(0))
        ator = Ator(0.3, 0.5)
        self.assertTupleEqual((0, 0), ator.calcular_posicao(2.3))
        ator = Ator(0.6, 2.1)
        self.assertTupleEqual((1, 2), ator.calcular_posicao(3.14))

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

    def assert_nao_colisao(self, ator, ator2):
        status_iniciais = [ator.status, ator2.status]
        self.assertFalse(ator.colidir(ator2))
        self.assertListEqual(status_iniciais, [ator.status, ator2.status])

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
        ator.status = DESTRUIDO
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

    def teste_status_dependete_de_tempo(self):
        ator = Ator()
        ator2 = Ator()

        self.assertEqual(ATIVO, ator.status)
        ator.colidir(ator2, 3.2)
        self.assertEqual('A', ator.calcular_posicao(0)[2])
        self.assertEqual(ATIVO,ator.status)
        self.assertEqual('A', ator.calcular_posicao(3.1)[2])
        self.assertEqual(ATIVO,ator.status)
        self.assertEqual('✝', ator.calcular_posicao(3.2)[2])
        self.assertEqual(ATIVO, Ator().status)


class ObstaculoTestes(TestCase):
    def teste_status(self):
        obstaculo = Obstaculo()
        self.assertEqual(ATIVO, obstaculo.status)
        self.assertEqual('O', obstaculo.calcular_posicao(0)[2])
        obstaculo.status = DESTRUIDO
        self.assertEqual(' ', obstaculo.calcular_posicao(0)[2])
        self.assertEqual(ATIVO, Ator().status)



