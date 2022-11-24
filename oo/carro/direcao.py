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
        self._valor = self._valor.obter_proximo_sentido_a_direita()

    def girar_a_esquerda(self) -> None:
        """
        Método girar_a_esquerda
            N
        O       L
            S
        """
        self._valor = self._valor.obter_proximo_sentido_a_esquerda()


class _Sentido(Enum):
    NORTE = 'Norte'
    SUL = 'Sul'
    LESTE = 'Leste'
    OESTE = 'Oeste'

    def obter_proximo_sentido_a_direita(self):
        mapa = {
            self.NORTE: self.LESTE,
            self.LESTE: self.SUL,
            self.SUL: self.OESTE,
            self.OESTE: self.NORTE
        }
        return mapa.get(self)

    def obter_proximo_sentido_a_esquerda(self):
        mapa = {
            self.NORTE: self.OESTE,
            self.OESTE: self.SUL,
            self.SUL: self.LESTE,
            self.LESTE: self.NORTE
        }
        return mapa.get(self)
