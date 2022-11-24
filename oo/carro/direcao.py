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
        self.valor: str = Sentido.NORTE.value


class Sentido(Enum):
    NORTE = 'Norte'
    SUL = 'Sul'
    LESTE = 'Leste'
    OESTE = 'Oeste'
