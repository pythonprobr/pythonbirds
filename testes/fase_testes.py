# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest.case import TestCase
from atores import Obstaculo, Porco, PassaroVermelho, PassaroAmarelo
from fase import Fase


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
        porcos = [Porco(1, 1) for i in range(2)]
        passaros = [PassaroAmarelo(1, 1) for i in range(2)]
        fase.adicionar_porco(*porcos)
        fase.adicionar_passaro(*passaros)
        self.assertFalse(fase.acabou(0))
        self.assertFalse(fase.acabou(2.9))
        self.assertFalse(fase.acabou(3))

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

        fase.adicionar_porco(Porco())
        self.assertEqual('Jogo em encerrado. Você perdeu!', fase.status(3),
                         'Com Porco ativo e sem pássaro para lançar, o jogo deveria acabar em derrota')

        fase.adicionar_passaro(PassaroAmarelo())
        self.assertEqual('Jogo em andamento.', fase.status(3),
                         'Com Porco ativo e com pássaro para lançar, o jogo não deveria acabar')


