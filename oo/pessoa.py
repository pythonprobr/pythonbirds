# -*- coding: utf-8 -*-

class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None,idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return 'f{cls} - olhos {olhos}'

class Homem(Pessoa):
    pass



if __name__ == "__main__":
    renzo = Pessoa(nome="Renzo", idade=35)
    fabio = Pessoa(renzo,nome="Fábio", idade=35)
    
    print(fabio.nome, fabio.idade)

    for filhos in fabio.filhos:
        print(filhos.nome)
        
    fabio.cidade = "Ribeirão Preto"
    print(fabio.cidade,"\n", fabio.__dict__)
    del fabio.cidade

