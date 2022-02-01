class Pessoa:
    def __init__(self, *filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

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
    print(luis.__dict__)
    print(fabio.__dict__)
