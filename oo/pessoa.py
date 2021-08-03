class Pessoa:
    def __init__(self, *filhos,nome=None, idade=26):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    paulo = Pessoa(nome='Paulo')
    henrique = Pessoa(paulo,nome='Henrique')
    print(Pessoa.cumprimentar(henrique))
    print(id(henrique))
    print(henrique.cumprimentar())
    print(henrique.nome)
    print(henrique.idade)
    for filho in henrique.filhos:
        print(filho.nome)