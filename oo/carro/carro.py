"""
Você deve criar classe carro que vai possuir atributos compostos por duas outras classes,
Motor e Direcao (a especificacao de cada estará nos seus arquivos correspondentes).

    >>> # Testando carro
    >>> direcao = Direcao()
    >>> motor = Motor()
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""
from oo.carro.motor import Motor
from oo.carro.direcao import Direcao


class Carro:
    def __init__(self, direcao: Direcao, motor: Motor) -> None:
        self._direcao = direcao
        self._motor = motor

    def calcular_velocidade(self) -> int:
        return self._motor.velocidade

    def acelerar(self) -> None:
        self._motor.acelerar()

    def frear(self) -> None:
        self._motor.frear()

    def calcular_direcao(self) -> str:
        return self._direcao.valor

    def girar_a_direita(self):
        self._direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self._direcao.girar_a_esquerda()
