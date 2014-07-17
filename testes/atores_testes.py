# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest.case import TestCase
from atores import Ator, DESTRUIDO, ATIVO, Obstaculo, Porco, PassaroAmarelo


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
        ator.colidir(ator, 0)
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


class PassaroBaseTests(TestCase):
    def assert_passaro_posicao(self, x_esperado, y_esperado, status_esperado, passaro, tempo):
        dct = {'x_esperado': x_esperado, 'y_esperado': y_esperado, 'status_esperado': status_esperado, 'tempo': tempo}
        self.assertTupleEqual((x_esperado, y_esperado), passaro.calcular_posicao(tempo), dct)
        passaro.colidir_com_chao(tempo)
        self.assertEqual(status_esperado, passaro.status(tempo), dct)


class PassaroAmareloTests(PassaroBaseTests):
    def teste_posicao_antes_do_lancamento(self):
        passaro_amarelo = PassaroAmarelo(1, 1)
        passaro_amarelo.lancar(90, 2)  # passaro lancado a 90 graus no tempo 2 segundos
        #
        for t in range(20):
            t /= 10
            self.assertEqual((1, 1), passaro_amarelo.calcular_posicao(t),
                             'Não deveria se mover no tempo %s < 2 segundtos' % t)

    def teste_status(self):
        passaro_amarelo = PassaroAmarelo(1, 1)
        assert_ator_status(self, passaro_amarelo, '>', '✝')

    def teste_colisao_com_chao(self):
        for i in range(30):
            passaro = PassaroAmarelo(i, 0)
            passaro.colidir_com_chao(3)
            self.assertEqual(DESTRUIDO, passaro.status(3), 'Deve colidir com chão sempre que y=0')

    def teste_lacamento_vertical(self):
        passaro_amarelo = PassaroAmarelo(1, 1)
        passaro_amarelo.lancar(90, 2)  # passaro lancado a 90 graus no tempo 2 segundos

        def assert_vertical(y_local, tempo):
            self.assert_passaro_posicao(1, y_local, ATIVO, passaro_amarelo, tempo)

        # subindo

        assert_vertical(1, 2.0)
        assert_vertical(1, 2.0)
        assert_vertical(1, 2.01)
        assert_vertical(2, 2.02)
        assert_vertical(2, 2.03)
        assert_vertical(2, 2.04)
        assert_vertical(2, 2.05)

        # descendo

        assert_vertical(46, 5.26)
        assert_vertical(46, 5.27)
        assert_vertical(46, 5.279999999999999)
        assert_vertical(46, 5.29)
        assert_vertical(46, 5.3)
        assert_vertical(46, 5.3100000000000005)
        assert_vertical(45, 5.32)
        assert_vertical(45, 5.33)
        assert_vertical(45, 5.34)
        assert_vertical(45, 5.35)
        assert_vertical(45, 5.359999999999999)
        assert_vertical(45, 5.37)
        assert_vertical(45, 5.38)
        assert_vertical(45, 5.390000000000001)
        assert_vertical(45, 5.4)
        assert_vertical(45, 5.41)
        assert_vertical(45, 5.42)
        assert_vertical(45, 5.43)
        assert_vertical(45, 5.4399999999999995)
        assert_vertical(45, 5.45)
        assert_vertical(45, 5.46)
        assert_vertical(45, 5.470000000000001)
        assert_vertical(45, 5.48)

        # preparando para impacto no chão
        assert_vertical(1, 8.0)
        assert_vertical(1, 8.01)

        # colisão
        self.assert_passaro_posicao(1, 0, DESTRUIDO, passaro_amarelo, 8.02)

    def lancamento_45_graus(self):
        pass
        # for delta_t in range(0, 1000):
        # t = 2 + (delta_t / 100)
        #     y=passaro_amarelo.calcular_posicao(t)[1]
        #     print('        assert_vertical(%s, %s)'%(y,t))

