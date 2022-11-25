"""
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear, que deverá decrementar a velocidade de duas unidades

    Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.frear()
    >>> motor.velocidade
    0

"""
__author__ = "Vinícius Salustiano"
__version__ = "0.1.0"


class Motor:
    def __init__(self) -> None:
        self._velocidade: int = 0

    def acelerar(self) -> None:
        """
        Método acelerar, que deverá incrementar a velocidade de uma unidade
        """
        self._velocidade += 1

    def frear(self) -> None:
        """
        Método frear, que deverá decrementar a velocidade de duas unidades

        Obs: velocidade não pode ficar negativa.
        """
        self._velocidade = max(0, self._velocidade - 2)

    @property
    def velocidade(self) -> int:
        return self._velocidade
