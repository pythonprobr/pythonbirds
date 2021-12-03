class Pessoa:
    def __init__(self, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
    def cumprimetar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Pereira')
    print(Pessoa.cumprimetar(p))
    print(id(p))
    print(p.cumprimetar())
    print(p.nome)
    p.nome = 'Josevaldo'
    print(p.nome)
    print(p.idade)
