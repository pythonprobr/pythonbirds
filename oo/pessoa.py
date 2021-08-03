class Pessoa:
    olhos = 2
    def __init__(self, *filhos,nome=None, idade=26):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'ola {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'



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
    henrique.sobrenome ='Lima'
    del henrique.filhos
    henrique.olhos = 1
    del henrique.olhos
    print(henrique.sobrenome)
    print(henrique.__dict__)
    print(paulo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(henrique.olhos)
    print(paulo.olhos)
    print(id(Pessoa.olhos),id(henrique.olhos),id(paulo.olhos))
    print(Pessoa.nome_e_atributos_de_classe(), henrique.nome_e_atributos_de_classe())