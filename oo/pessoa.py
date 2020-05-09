# -*- coding: utf-8 -*-

class Pessoa:
    def __init__(self, *filhos, nome=None,idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == "__main__":
    renzo = Pessoa(nome="Renzo", idade=35)
    fabio = Pessoa(renzo,nome="Fábio", idade=35)
    
    print(fabio.nome, fabio.idade)

    for filhos in fabio.filhos:
        print(filhos.nome)
        
    fabio.cidade = "Ribeirão Preto"
    print(fabio.cidade,"\n", fabio.__dict__)
    del fabio.cidade

