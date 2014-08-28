# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import math

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'


class Ator():
    _caracter_ativo = 'A'
    _caracter_destruido = ' '

    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x
        self._tempo_de_colisao = None

    def caracter(self, tempo):
        return self._caracter_ativo if self.status(tempo) == ATIVO else self._caracter_destruido

    def resetar(self):
        self._tempo_de_colisao = None

    def status(self, tempo):
        if self._tempo_de_colisao is None or self._tempo_de_colisao > tempo:
            return ATIVO
        return DESTRUIDO

    def calcular_posicao(self, tempo):
        return self.arredondar_posicao()

    def arredondar_posicao(self):
        self.x, self.y = round(self.x), round(self.y)
        return self.x, self.y

    def colidir(self, outro_ator, tempo, intervalo=1):
        if self.status(tempo) == DESTRUIDO or outro_ator.status(tempo) == DESTRUIDO:
            return
        x1, y1 = self.arredondar_posicao()
        x2, y2 = outro_ator.arredondar_posicao()

        if x1 - intervalo <= x2 <= x1 + intervalo and y1 - intervalo <= y2 <= y1 + intervalo:
            self._tempo_de_colisao = tempo
            outro_ator._tempo_de_colisao = tempo


class Obstaculo(Ator):
    _caracter_ativo = 'O'


class Porco(Ator):
    _caracter_ativo = '@'
    _caracter_destruido = '+'


GRAVIDADE = 10  # m/s^2


class Passaro(Ator):
    velocidade_escalar = None

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._x_inicial = x
        self._y_inicial = y
        self._tempo_de_lancamento = None
        self._angulo_de_lancamento = None  # radianos

    def resetar(self):
        super().resetar()
        self._tempo_de_lancamento = None
        self._angulo_de_lancamento = None


    def foi_lancado(self):
        return self._tempo_de_lancamento is not None

    def colidir_com_chao(self, tempo):
        if self.y <= 0:
            self._tempo_de_colisao = tempo

    def _calcular_posicao_horizontal(self, delta_t):
        self.x = self._x_inicial + self.velocidade_escalar * delta_t * math.cos(self._angulo_de_lancamento)

    def _calcular_posicao_vertical(self, delta_t):
        self.y = (self._y_inicial +
                  self.velocidade_escalar * delta_t * math.sin(self._angulo_de_lancamento) -
                  (GRAVIDADE / 2) * delta_t ** 2)

    def _calcular_posicao(self, tempo):
        delta_t = tempo - self._tempo_de_lancamento
        self._calcular_posicao_vertical(delta_t)
        self._calcular_posicao_horizontal(delta_t)

    def calcular_posicao(self, tempo):
        if self._aguardando_lancamento(tempo):
            self.x = self._x_inicial
            self.y = self._y_inicial
        elif self._ja_colidiu(tempo):
            self._calcular_posicao(self._tempo_de_colisao)
        else:
            self._calcular_posicao(tempo)
        return self.arredondar_posicao()

    def lancar(self, angulo, tempo):
        self._tempo_de_lancamento = tempo
        self._angulo_de_lancamento = math.radians(angulo)

    def _aguardando_lancamento(self, tempo):
        return not self.foi_lancado() or tempo < self._tempo_de_lancamento

    def _ja_colidiu(self, tempo):
        return self.foi_lancado() and self.status(tempo) == DESTRUIDO


class PassaroAmarelo(Passaro):
    velocidade_escalar = 30  # m/s
    _caracter_ativo = 'A'
    _caracter_destruido = 'a'


class PassaroVermelho(Passaro):
    velocidade_escalar = 20  # m/s
    _caracter_ativo = 'V'
    _caracter_destruido = 'v'
