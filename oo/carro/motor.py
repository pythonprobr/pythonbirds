"""
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear, que deverá decrementar a velocidade de duas unidades
"""
__author__ = "Vinícius Salustiano"
__version__ = "0.1.0"


class Motor:
    def __init__(self) -> None:
        self.velocidade: int = 0
