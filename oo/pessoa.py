"""
Modelo para aprendizado de orientação a objetos em Python.
"""
__author__ = "Vinícius Salustiano"
__version__ = "0.1.0"

from typing import List


class Pessoa:

    olhos: int = 2

    def __init__(self, *filhos, nome: str) -> None:
        self.nome = nome
        self.filhos: List[Pessoa] = list(filhos)

    def cumprimentar(self) -> str:
        """
        Retorna uma str com cumprimento a quem invocou a mensagem.
        """
        return f'Olá, sou {self.nome}'

    @staticmethod
    def metodo_estatico() -> int:
        return 42

    @classmethod
    def metodo_classe(cls) -> str:
        return f'Número de olhos: {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self) -> str:
        return super().cumprimentar() + ". Aperto de mão."


if __name__ == '__main__':
    renzo = Homem(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(luciano.cumprimentar())
    for filho in luciano.filhos:
        print(filho.cumprimentar())
    print(Pessoa.metodo_estatico())
    print(Pessoa.metodo_classe())
