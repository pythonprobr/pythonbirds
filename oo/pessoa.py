class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_aributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    fabio = Pessoa(nome='Fabio')
    luis = Pessoa(fabio, nome='Luis')
    print(Pessoa.cumprimentar(luis))
    print(id(luis))
    print(luis.cumprimentar())
    print(luis.nome)
    print(luis.idade)
    for filho in luis.filhos:
        print(filho.nome)
    luis.sobrenome = 'Santos da Silva'
    del luis.filhos
    luis.olhos = 1
    del luis.olhos
    print(luis.__dict__)
    print(fabio.__dict__)
    print(Pessoa.olhos)
    print(luis.olhos)
    print(fabio.olhos)
    print(id(Pessoa.olhos), id(luis.olhos), id(fabio.olhos))
    print(Pessoa.metodo_estatico(), luis.metodo_estatico())
    print(Pessoa.nome_e_aributos_de_classe(), luis.nome_e_aributos_de_classe())