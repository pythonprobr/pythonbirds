# -*- coding: utf-8 -*-

import os
import sys
from os import path
from unittest.case import TestCase

project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)
from placa_grafica_tkinter import rodar_fase

project_dir = os.path.join(os.path.dirname(__file__), '..')
project_dir = os.path.normpath(project_dir)
sys.path.append(project_dir)

from atores import (Obstaculo, Porco, PassaroVermelho, PassaroAmarelo,
                    DESTRUIDO, ATIVO, DuploLancamentoExcecao)
from fase import Fase, Ponto, EM_ANDAMENTO, VITORIA, DERROTA


class AtorFake:
    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x
        self.status = ATIVO
        self.colidir_executado = False
        self.calcular_posicao_executado = False
        self.intervalo_colisao = None

    def calcular_posicao(self, tempo):
        self.calcular_posicao_executado = True

    def colidir(self, outro_ator, intervalo):
        self.colidir_executado = outro_ator.colidir_executado = True
        self.intervalo_colisao = outro_ator.intervalo_colisao = intervalo

    def caracter(self):
        return ' '


class ObstaculoFake(AtorFake):
    pass


class PorcoFake(AtorFake):
    pass


class PassaroFake(AtorFake):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._lancado = False
        self.colidir_com_chao_executado = False

    def foi_lancado(self):
        return self._lancado

    def lancar(self, angulo, tempo):
        if self._lancado:
            raise DuploLancamentoExcecao()
        self._lancado = True

    def colidir_com_chao(self):
        self.colidir_com_chao_executado = True


class FaseTestes(TestCase):
    def teste_adicionar_obstaculo(self):
        fase = Fase()
        self.assertListEqual([], fase._obstaculos)
        obstaculo = ObstaculoFake()
        fase.adicionar_obstaculo(obstaculo)
        self.assertListEqual([obstaculo], fase._obstaculos)

        obstaculo1, obstaculo2 = ObstaculoFake(), ObstaculoFake()
        fase.adicionar_obstaculo(obstaculo1, obstaculo2)
        self.assertListEqual([obstaculo, obstaculo1, obstaculo2],
                             fase._obstaculos)

    def teste_adicionar_porco(self):
        fase = Fase()
        self.assertListEqual([], fase._porcos)
        porco = PorcoFake()
        fase.adicionar_porco(porco)
        self.assertListEqual([porco], fase._porcos)

        porco1, porco2 = PorcoFake(), PorcoFake()
        fase.adicionar_porco(porco1, porco2)
        self.assertListEqual([porco, porco1, porco2], fase._porcos)

    def teste_adicionar_passaro(self):
        fase = Fase()
        self.assertListEqual([], fase._passaros)
        passaro = PassaroFake()
        fase.adicionar_passaro(passaro)
        self.assertListEqual([passaro], fase._passaros)

        passaro1, passaro2 = PassaroFake(), PassaroFake()
        fase.adicionar_passaro(passaro1, passaro2)
        self.assertListEqual([passaro, passaro1, passaro2], fase._passaros)

    def teste_acabou_sem_porcos(self):
        fase = Fase()
        self.assertEqual(VITORIA, fase.status())

    def teste_acabou_com_porcos_e_passaros(self):
        fase = Fase()
        porcos = [PorcoFake(1, 1) for _ in range(2)]  # criando 2 porcos
        passaros = [PassaroFake(1, 1) for _ in range(2)]  # criando 2 pássaros
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)

        self.assertEqual(EM_ANDAMENTO, fase.status())

        for ator in porcos + passaros:
            ator.status = DESTRUIDO
        self.assertEqual(VITORIA, fase.status())

        fase.adicionar_obstaculo(Obstaculo())
        self.assertEqual(VITORIA, fase.status(),
                         'Obstáculo não interfere no fim do jogo')

        fase.adicionar_porco(PorcoFake())
        self.assertEqual(DERROTA, fase.status(),
                         'Com Porco ativo e sem pássaro para lançar, o jogo '
                         'deveria acabar')

        fase.adicionar_passaro(PassaroFake())
        self.assertEqual(EM_ANDAMENTO, fase.status(),
                         'Com Porco ativo e com pássaro para lançar, o jogo '
                         'não deveria acabar')

    def teste_status(self):
        fase = Fase()
        porcos = [PorcoFake(1, 1) for _ in range(2)]
        passaros = [PassaroFake(1, 1) for _ in range(2)]
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)
        self.assertEqual(EM_ANDAMENTO, fase.status())

        for ator in porcos + passaros:
            ator.status = DESTRUIDO
        self.assertEqual(VITORIA, fase.status(),
                         'Sem porcos ativos o jogo deveria terminar com '
                         'vitória')

        fase.adicionar_obstaculo(ObstaculoFake())
        self.assertEqual(VITORIA, fase.status(),
                         'Obstáculo não interfere para definir vitória')

        porco = PorcoFake()
        fase.adicionar_porco(porco)
        self.assertEqual(DERROTA, fase.status(),
                         'Com Porco ativo e sem pássaro para lançar, o jogo '
                         'deveria acabar em derrota')

        fase.adicionar_passaro(PassaroFake())
        self.assertEqual(EM_ANDAMENTO, fase.status(),
                         'Com Porco ativo e com pássaro para lançar, o jogo '
                         'não deveria acabar')

        porco.status = DESTRUIDO
        self.assertEqual(VITORIA, fase.status(),
                         'Sem porco ativo, o jogo deveria acabar com vitória')

    def teste_lancar_passaro_sem_erro_quando_nao_existe_passaro(self):
        passaros = [PassaroFake(1, 1) for _ in range(2)]
        fase = Fase()
        fase.adicionar_passaro(*passaros)
        self.assertFalse(passaros[0].foi_lancado())
        self.assertFalse(passaros[1].foi_lancado())
        fase.lancar(90, 1)
        fase.lancar(45, 3)
        fase.lancar(31,
                    5)  # testando que lançar passaros depios de todos
        # lançados não causa erro

        self.assertTrue(passaros[0].foi_lancado())
        self.assertTrue(passaros[1].foi_lancado())

    def teste_intervalo_de_colisao_padrao(self):
        '''
        Método que testa se o intervalo de colisão da Fase é repassado aos
        atores. Padrão de intervalo é 1
        '''
        fase = Fase()
        passaro = PassaroFake(1, 1)
        fase.adicionar_passaro(passaro)
        porco = PorcoFake(2, 2)
        fase.adicionar_porco(porco)
        fase.calcular_pontos(0)
        self.assertTrue(passaro.colidir_executado)
        self.assertTrue(porco.colidir_executado)
        self.assertTrue(passaro.calcular_posicao_executado)
        self.assertTrue(passaro.colidir_com_chao_executado)
        self.assertEqual(1, passaro.intervalo_colisao)
        self.assertEqual(1, porco.intervalo_colisao)

    def teste_intervalo_de_colisao_nao_padrao(self):
        '''
        Método que testa se o intervalo de colisão da Fase é repassado aos
        atores. valor testado: 31
        '''
        fase = Fase(30)
        passaro = PassaroFake(1, 1)
        fase.adicionar_passaro(passaro)
        porco = PorcoFake(31, 31)
        fase.adicionar_porco(porco)
        fase.calcular_pontos(0)
        self.assertEqual(30, passaro.intervalo_colisao)
        self.assertEqual(30, porco.intervalo_colisao)
