"""
Modelo para aprendizado de orientação a objetos em Python.
"""
__author__ = "Vinícius Salustiano"
__version__ = "0.1.0"


class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def cumprimentar(self) -> str:
        """
        Retorna uma str com cumprimento a quem invocou a mensagem.
        """
        return f'Olá, sou {self.nome}'


if __name__ == '__main__':
    pessoa = Pessoa('Renzo')
    print(pessoa.cumprimentar())
