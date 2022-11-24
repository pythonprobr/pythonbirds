"""
Modelo para aprendizado de orientação a objetos em Python.
"""
__author__ = "Vinícius Salustiano"
__version__ = "0.1.0"

from typing import List


class Pessoa:
    def __init__(self, *filhos, nome: str) -> None:
        self.nome = nome
        self.filhos: List[Pessoa] = list(filhos)

    def cumprimentar(self) -> str:
        """
        Retorna uma str com cumprimento a quem invocou a mensagem.
        """
        return f'Olá, sou {self.nome}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(luciano.cumprimentar())
    for filho in luciano.filhos:
        print(filho.cumprimentar())
