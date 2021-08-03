class Pessoa:
    def __init__(self, nome=None, idade=26):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('henrique')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'paulo'
    print(p.nome)
    print(p.idade)
