# -*- coding: utf-8 -*-
from itertools import chain

import os
from unittest.case import TestCase
import math
import sys

project_dir = os.path.join(os.path.dirname(__file__), '..')
project_dir = os.path.normpath(project_dir)
sys.path.append(project_dir)

from atores import Obstaculo, Porco, PassaroVermelho, PassaroAmarelo, DESTRUIDO, ATIVO
from fase import Fase, Ponto
import placa_grafica


class FaseTestes(TestCase):
    def teste_adicionar_obstaculo(self):
        fase = Fase()
        self.assertListEqual([], fase._obstaculos)
        obstaculo = Obstaculo()
        fase.adicionar_obstaculo(obstaculo)
        self.assertListEqual([obstaculo], fase._obstaculos)

        obstaculo1, obstaculo2 = Obstaculo(), Obstaculo()
        fase.adicionar_obstaculo(obstaculo1, obstaculo2)
        self.assertListEqual([obstaculo, obstaculo1, obstaculo2], fase._obstaculos)

    def teste_adicionar_porco(self):
        fase = Fase()
        self.assertListEqual([], fase._porcos)
        porco = Porco()
        fase.adicionar_porco(porco)
        self.assertListEqual([porco], fase._porcos)

        porco1, porco2 = Porco(), Porco()
        fase.adicionar_porco(porco1, porco2)
        self.assertListEqual([porco, porco1, porco2], fase._porcos)

    def teste_adicionar_passaro(self):
        fase = Fase()
        self.assertListEqual([], fase._passaros)
        passaro = PassaroVermelho()
        fase.adicionar_passaro(passaro)
        self.assertListEqual([passaro], fase._passaros)

        passaro1, passaro2 = PassaroVermelho(), PassaroAmarelo()
        fase.adicionar_passaro(passaro1, passaro2)
        self.assertListEqual([passaro, passaro1, passaro2], fase._passaros)


    def teste_acabou_sem_porcos(self):
        fase = Fase()
        self.assertTrue(fase.acabou(0))

    def teste_acabou_com_porcos_e_passaros(self):
        fase = Fase()
        porcos = [Porco(1, 1) for i in range(2)]  # criando 2 porcos
        passaros = [PassaroAmarelo(1, 1) for i in range(2)]  # criando 2 pássaros
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)

        self.assertFalse(fase.acabou(0))
        self.assertFalse(fase.acabou(2.9))
        self.assertFalse(fase.acabou(3))

        # colidingo cada passaro com um porco no tempo 3
        for passaro, porco in zip(passaros, porcos):
            passaro.colidir(porco, 3)

        self.assertFalse(fase.acabou(0))
        self.assertFalse(fase.acabou(2.9))
        self.assertTrue(fase.acabou(3))

        fase.adicionar_obstaculo(Obstaculo())
        self.assertTrue(fase.acabou(3), 'Obstáculo não interfere no fim do jogo')

        fase.adicionar_porco(Porco())
        self.assertTrue(fase.acabou(3), 'Com Porco ativo e sem pássaro para lançar, o jogo deveria acabar')

        fase.adicionar_passaro(PassaroAmarelo())
        self.assertFalse(fase.acabou(3), 'Com Porco ativo e com pássaro para lançar, o jogo não deveria acabar')

    def teste_status(self):
        fase = Fase()
        porcos = [Porco(1, 1) for i in range(2)]
        passaros = [PassaroAmarelo(1, 1) for i in range(2)]
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)
        self.assertEqual('Jogo em andamento.', fase.status(0))
        self.assertEqual('Jogo em andamento.', fase.status(2.9))
        self.assertEqual('Jogo em andamento.', fase.status(3))

        for passaro, porco in zip(passaros, porcos):
            passaro.colidir(porco, 3)

        self.assertEqual('Jogo em andamento.', fase.status(0))
        self.assertEqual('Jogo em andamento.', fase.status(2.9))
        self.assertEqual('Jogo em encerrado. Você ganhou!', fase.status(3),
                         'Sem porcos ativos o jogo deveria terminar com vitória')

        fase.adicionar_obstaculo(Obstaculo())
        self.assertEqual('Jogo em encerrado. Você ganhou!', fase.status(3),
                         'Obstáculo não interfere para definir vitória')

        porco = Porco()
        fase.adicionar_porco(porco)
        self.assertEqual('Jogo em encerrado. Você perdeu!', fase.status(3),
                         'Com Porco ativo e sem pássaro para lançar, o jogo deveria acabar em derrota')

        fase.adicionar_passaro(PassaroAmarelo())
        self.assertEqual('Jogo em andamento.', fase.status(3),
                         'Com Porco ativo e com pássaro para lançar, o jogo não deveria acabar')

        porco.colidir(porco, 3)
        self.assertEqual('Jogo em encerrado. Você ganhou!', fase.status(3),
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
        self.assertEqual(DESTRUIDO, passaro.status(0))
        self.assertEqual(DESTRUIDO, porco.status(0))

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
        self.assertEqual(DESTRUIDO, passaro.status(0))
        self.assertEqual(DESTRUIDO, porco.status(0))

    def teste_calcular_pontos(self):
        fase_exemplo = criar_fase_exemplo()
        expected = [Ponto(3, 3, 'V'), Ponto(3, 3, 'A'), Ponto(3, 3, 'A'), Ponto(31, 10, 'O'), Ponto(78, 1, '@'),
                    Ponto(70, 1, '@')]
        self.assertListEqual(expected, fase_exemplo.calcular_pontos(0))

        expected = [Ponto(31, 11, 'v'), Ponto(17, 25, 'A'), Ponto(3, 3, 'A'), Ponto(31, 10, ' '), Ponto(78, 1, '@'),
                    Ponto(70, 1, '@')]
        self.assertListEqual(expected, fase_exemplo.calcular_pontos(4))

        expected = [Ponto(31, 11, 'v'), Ponto(57, 30, 'A'), Ponto(69, 2, 'a'), Ponto(31, 10, ' '), Ponto(78, 1, '@'),
                    Ponto(70, 1, '+')]
        self.assertListEqual(expected, fase_exemplo.calcular_pontos(7))

        expected = [Ponto(31, 11, 'v'), Ponto(77, 2, 'a'), Ponto(69, 2, 'a'), Ponto(31, 10, ' '), Ponto(78, 1, '+'),
                    Ponto(70, 1, '+')]
        self.assertListEqual(expected, fase_exemplo.calcular_pontos(8.5))

        self.assertFalse(fase_exemplo.acabou(8.3))
        self.assertTrue(fase_exemplo.acabou(8.5))

    def teste_resetar(self):
        'Testa se o método resetar de faze chama o método resetar de todos atores'
        fase_exemplo = criar_fase_exemplo()
        atores = list(chain(fase_exemplo._passaros, fase_exemplo._obstaculos, fase_exemplo._porcos))
        fase_exemplo.calcular_pontos(0)

        fase_exemplo.calcular_pontos(4)

        fase_exemplo.calcular_pontos(7)
        fase_exemplo.calcular_pontos(8.5)

        self.assertFalse(fase_exemplo.acabou(8.3))
        self.assertTrue(fase_exemplo.acabou(8.5))
        # certificando que todos atore foram destruidos
        for a in atores:
            self.assertEqual(DESTRUIDO, a.status(8.5))
        for p in fase_exemplo._passaros:
            self.assertTrue(p.foi_lancado(), 'Todos pássaros foram lançados')
        fase_exemplo.resetar()
        for a in atores:
            self.assertEqual(ATIVO, a.status(8.5), 'Após resetar atore devem voltar a ficar ativos')
        for p in fase_exemplo._passaros:
            self.assertFalse(p.foi_lancado(), 'Nenhum pássaro foi lançado')


def criar_fase_exemplo():
    fase_exemplo = Fase()
    passaros = [PassaroVermelho(3, 3), PassaroAmarelo(3, 3), PassaroAmarelo(3, 3)]
    porcos = [Porco(78, 1), Porco(70, 1)]
    obstaculos = [Obstaculo(31, 10)]

    fase_exemplo.adicionar_passaro(*passaros)
    fase_exemplo.adicionar_porco(*porcos)
    fase_exemplo.adicionar_obstaculo(*obstaculos)

    fase_exemplo.lancar(45, 1)
    fase_exemplo.lancar(63, 3)
    fase_exemplo.lancar(23, 4)

    for i in range(86):
        fase_exemplo.calcular_pontos(i / 10)
    return fase_exemplo


if __name__ == '__main__':
    placa_grafica.animar(criar_fase_exemplo())
