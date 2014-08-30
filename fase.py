# -*- coding: utf-8 -*-
from itertools import chain
from atores import ATIVO


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    def __init__(self, intervalo_de_colisao=1):
        self.intervalo_de_colisao = intervalo_de_colisao
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

    def _adicionar_ator(self, lista, *atores):
        lista.extend(atores)

    def adicionar_obstaculo(self, *obstaculos):
        self._adicionar_ator(self._obstaculos, *obstaculos)

    def adicionar_porco(self, *porcos):
        self._adicionar_ator(self._porcos, *porcos)

    def adicionar_passaro(self, *passaros):
        self._adicionar_ator(self._passaros, *passaros)

    def acabou(self):
        return not self._existe_porco_ativo() or not self._existe_passaro_ativo()

    def status(self):
        if not self._existe_porco_ativo():
            return 'Jogo em encerrado. Você ganhou!'
        if self._existe_passaro_ativo():
            return 'Jogo em andamento.'
        return 'Jogo em encerrado. Você perdeu!'

    def lancar(self, angulo, tempo):
        for passaro in self._passaros:
            if not passaro.foi_lancado():
                passaro.lancar(angulo, tempo)
                return


    def calcular_pontos(self, tempo):
        pontos = [self._calcular_ponto_de_passaro(p, tempo) for p in self._passaros]
        obstaculos_e_porcos = chain(self._obstaculos, self._porcos)
        pontos.extend([self._transformar_em_ponto(ator) for ator in obstaculos_e_porcos])
        return pontos

    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter)

    def _calcular_ponto_de_passaro(self, passaro, tempo, ):
        passaro.calcular_posicao(tempo)
        for ator in chain(self._obstaculos, self._porcos):
            if ATIVO == passaro.status:
                passaro.colidir(ator, self.intervalo_de_colisao)
                passaro.colidir_com_chao()
            else:
                break
        return self._transformar_em_ponto(passaro)

    def _existe_porco_ativo(self):
        return self._verificar_se_existe_ator_ativo(self._porcos)

    def _verificar_se_existe_ator_ativo(self, atores):
        for a in atores:
            if a.status == ATIVO:
                return True
        return False

    def _existe_passaro_ativo(self):
        return self._verificar_se_existe_ator_ativo(self._passaros)
