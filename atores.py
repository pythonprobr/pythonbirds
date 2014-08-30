# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import math

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'
GRAVIDADE = 10  # m/s^2


class Ator():
    _caracter_ativo = 'A'
    _caracter_destruido = ' '

    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x
        self.caracter = self._caracter_ativo
        self.status = ATIVO

    def calcular_posicao(self, tempo):
        return self.x, self.y

    def colidir(self, outro_ator, intervalo=1):
        if self.status == DESTRUIDO or outro_ator.status == DESTRUIDO:
            return

        if self.x - intervalo <= outro_ator.x <= self.x + intervalo and self.y - intervalo <= outro_ator.y <= self.y + intervalo:
            self.status = DESTRUIDO
            self.caracter = self._caracter_destruido
            outro_ator.caracter = outro_ator._caracter_destruido
            outro_ator.status = DESTRUIDO


class Obstaculo(Ator):
    _caracter_ativo = 'O'


class Porco(Ator):
    _caracter_ativo = '@'
    _caracter_destruido = '+'


class Passaro(Ator):
    velocidade_escalar = None

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._x_inicial = x
        self._y_inicial = y
        self._tempo_de_lancamento = None
        self._angulo_de_lancamento = None  # radianos

    def foi_lancado(self):
        return self._tempo_de_lancamento is not None

    def colidir_com_chao(self):
        if self.y <= 0:
            self.status = DESTRUIDO

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
        if self._tempo_de_lancamento is None:
            return self._x_inicial, self._y_inicial
        if self.status == ATIVO:
            self._calcular_posicao(tempo)
        return self.x, self.y


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
