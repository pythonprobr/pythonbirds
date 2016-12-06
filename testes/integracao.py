# -*- coding: utf-8 -*-
from itertools import chain

import os
from os import path
from unittest.case import TestCase
import math
import sys

project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)
from placa_grafica_tkinter import rodar_fase

project_dir = os.path.join(os.path.dirname(__file__), '..')
project_dir = os.path.normpath(project_dir)
sys.path.append(project_dir)

from atores import Obstaculo, Porco, PassaroVermelho, PassaroAmarelo, DESTRUIDO, ATIVO, \
    Ator, Passaro
from fase import Fase, Ponto, EM_ANDAMENTO, VITORIA, DERROTA

class FaseTestes(TestCase):
    def teste_acabou_com_porcos_e_passaros(self):
        fase = Fase()
        porcos = [Porco(1, 1) for i in range(2)]  # criando 2 porcos
        passaros = [PassaroAmarelo(1, 1) for i in range(2)]  # criando 2 pássaros
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)

        self.assertEqual(EM_ANDAMENTO, fase.status())

        # colidindo cada passaro com um porco no tempo 3
        for passaro, porco in zip(passaros, porcos):
            passaro.colidir(porco, 3)

        self.assertEqual(VITORIA, fase.status())

        fase.adicionar_obstaculo(Obstaculo())
        self.assertEqual(VITORIA, fase.status(), 'Obstáculo não interfere no fim do jogo')

        fase.adicionar_porco(Porco())
        self.assertEqual(DERROTA, fase.status(), 'Com Porco ativo e sem pássaro para lançar, o jogo deveria acabar')

        fase.adicionar_passaro(PassaroAmarelo())
        self.assertEqual(EM_ANDAMENTO, fase.status(),
                         'Com Porco ativo e com pássaro para lançar, o jogo não deveria acabar')

    def teste_status(self):
        fase = Fase()
        porcos = [Porco(1, 1) for i in range(2)]
        passaros = [PassaroAmarelo(1, 1) for i in range(2)]
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)
        self.assertEqual(EM_ANDAMENTO, fase.status())

        for passaro, porco in zip(passaros, porcos):
            passaro.colidir(porco, 3)

        self.assertEqual(VITORIA, fase.status(),
                         'Sem porcos ativos o jogo deveria terminar com vitória')

        fase.adicionar_obstaculo(Obstaculo())
        self.assertEqual(VITORIA, fase.status(),
                         'Obstáculo não interfere para definir vitória')

        porco = Porco()
        fase.adicionar_porco(porco)
        self.assertEqual(DERROTA, fase.status(),
                         'Com Porco ativo e sem pássaro para lançar, o jogo deveria acabar em derrota')

        fase.adicionar_passaro(PassaroAmarelo())
        self.assertEqual(EM_ANDAMENTO, fase.status(),
                         'Com Porco ativo e com pássaro para lançar, o jogo não deveria acabar')

        porco.colidir(porco, 3)
        self.assertEqual(VITORIA, fase.status(),
                         'Sem porco ativo, o jogo deveria acabar com vitória')

    def teste_lancar_passaro_sem_erro_quando_nao_existe_passaro(self):
        passaro_vermelho, passaro_amarelo = PassaroVermelho(1, 1), PassaroAmarelo(1, 1)
        fase = Fase()
        fase.adicionar_passaro(passaro_vermelho, passaro_amarelo)
        self.assertFalse(passaro_vermelho.foi_lancado())
        self.assertFalse(passaro_amarelo.foi_lancado())
        fase.lancar(90, 1)
        fase.lancar(45, 3)
        fase.lancar(31, 5)  # testando que lançar passaros depios de todos lançados não causa erro

        self.assertTrue(passaro_vermelho.foi_lancado())
        self.assertEqual(math.radians(90), passaro_vermelho._angulo_de_lancamento)
        self.assertEqual(1, passaro_vermelho._tempo_de_lancamento)

        self.assertTrue(passaro_amarelo.foi_lancado())
        self.assertEqual(math.radians(45), passaro_amarelo._angulo_de_lancamento)
        self.assertEqual(3, passaro_amarelo._tempo_de_lancamento)

    def teste_intervalo_de_colisao_padrão(self):
        '''
        Método que testa se o intervalo de colisão da Fase é repassado aos atores. Padrão de intervalo é 1
        '''
        fase = Fase()
        passaro = PassaroAmarelo(1, 1)
        fase.adicionar_passaro(passaro)
        porco = Porco(2, 2)
        fase.adicionar_porco(porco)
        fase.calcular_pontos(0)
        self.assertEqual(DESTRUIDO, passaro.status)
        self.assertEqual(DESTRUIDO, porco.status)

    def teste_intervalo_de_colisao_nao_padrao(self):
        '''
        Método que testa se o intervalo de colisão da Fase é repassado aos atores. valor testado: 31
        '''
        fase = Fase(30)
        passaro = PassaroAmarelo(1, 1)
        fase.adicionar_passaro(passaro)
        porco = Porco(31, 31)
        fase.adicionar_porco(porco)
        fase.calcular_pontos(0)
        self.assertEqual(DESTRUIDO, passaro.status)
        self.assertEqual(DESTRUIDO, porco.status)

    def teste_calcular_pontos(self):
        fase_exemplo = criar_fase_exemplo()
        expected = set([Ponto(3, 3, 'A'), Ponto(3, 3, 'A'), Ponto(31, 10, 'O'), Ponto(78, 1, '@'),
                        Ponto(70, 1, '@'), Ponto(3, 3, 'V')])
        self.assertSetEqual(expected, set(fase_exemplo.calcular_pontos(0)))

        fase_exemplo.lancar(45, 1)

        # i variando de 1 até 2.9
        for i in range(100, 300, 1):
            fase_exemplo.calcular_pontos(i / 100)

        fase_exemplo.lancar(63, 3)

        # i variando de 3 até 3.9
        for i in range(300, 400, 1):
            fase_exemplo.calcular_pontos(i / 100)

        fase_exemplo.lancar(23, 4)

        expected = set([Ponto(32, 11, 'v'), Ponto(17, 25, 'A'), Ponto(3, 3, 'A'), Ponto(31, 10, ' '), Ponto(78, 1, '@'),
                        Ponto(70, 1, '@')])

        self.assertSetEqual(expected, set(fase_exemplo.calcular_pontos(4)))

        # i variando de 4 até 6.9
        for i in range(400, 700, 1):
            fase_exemplo.calcular_pontos(i / 100)

        expected = set(
            [Ponto(32, 11, 'v'), Ponto(57, 30, 'A'), Ponto(70, 2, 'a'), Ponto(31, 10, ' '), Ponto(78, 1, '@'),
             Ponto(70, 1, '+')])

        self.assertSetEqual(expected, set(fase_exemplo.calcular_pontos(7)))

        # i variando de 7 até 8.49
        for i in range(700, 849, 1):
            fase_exemplo.calcular_pontos(i / 100)
        print(fase_exemplo.calcular_pontos(8.5))

        expected = set([Ponto(32, 11, 'v'), Ponto(77, 0, 'a'), Ponto(70, 2, 'a'), Ponto(31, 10, ' '), Ponto(78, 1, '+'),
                        Ponto(70, 1, '+')])

        self.assertSetEqual(expected, set(fase_exemplo.calcular_pontos(8.5)))

        self.assertEqual(VITORIA, fase_exemplo.status())


def criar_fase_exemplo(multiplicador=1):
    fase_exemplo = Fase(1 if multiplicador == 1 else 32)
    passaros = [PassaroVermelho(3 * multiplicador, 3 * multiplicador),
                PassaroAmarelo(3 * multiplicador, 3 * multiplicador),
                PassaroAmarelo(3 * multiplicador, 3 * multiplicador)]
    porcos = [Porco(78 * multiplicador, multiplicador), Porco(70 * multiplicador, multiplicador)]
    obstaculos = [Obstaculo(31 * multiplicador, 10 * multiplicador)]

    fase_exemplo.adicionar_passaro(*passaros)
    fase_exemplo.adicionar_porco(*porcos)
    fase_exemplo.adicionar_obstaculo(*obstaculos)

    return fase_exemplo


if __name__ == '__main__':
    rodar_fase(criar_fase_exemplo(10))
