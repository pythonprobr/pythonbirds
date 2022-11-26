"""
A Direção terá a responsabilidade de controlar a direção. Ela
oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste e Oeste
2) Método girar_a_direita
3) Método girar_a_esquerda
    N
O       L
    S

Exemplo:

    >>> # Testando a direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
"""
__author__ = "Vinícius Salustiano"
__version__ = "0.1.0"

from enum import Enum


class Direcao:

    def __init__(self):
        self._valor: _Sentido = _Sentido.NORTE
        self._navegador_sentidos: _NavegadorSentido = _NavegadorSentido()

    @property
    def valor(self) -> str:
        return str(self._valor.value)

    def girar_a_direita(self) -> None:
        """
        2) Método girar_a_direita
                N
            O       L
                S
        """
        self._valor = self._navegador_sentidos.sentido_direita(self._valor)

    def girar_a_esquerda(self) -> None:
        """
        Método girar_a_esquerda
            N
        O       L
            S
        """
        self._valor = self._navegador_sentidos.sentido_esquerda(self._valor)


class _Sentido(Enum):
    NORTE = 'Norte'
    SUL = 'Sul'
    LESTE = 'Leste'
    OESTE = 'Oeste'


class _No:
    def __init__(self, esquerda, direita) -> None:
        self.esquerda = esquerda
        self.direita = direita


class _NavegadorSentido:
    def __init__(self) -> None:
        self._mapa = {
            _Sentido.NORTE: _No(_Sentido.OESTE, _Sentido.LESTE),
            _Sentido.LESTE: _No(_Sentido.NORTE, _Sentido.SUL),
            _Sentido.SUL: _No(_Sentido.LESTE, _Sentido.OESTE),
            _Sentido.OESTE: _No(_Sentido.SUL, _Sentido.NORTE)
        }

    def sentido_esquerda(self, sentido: _Sentido) -> _Sentido:
        return self._mapa.get(sentido).esquerda

    def sentido_direita(self, sentido: _Sentido) -> _Sentido:
        return self._mapa.get(sentido).direita
