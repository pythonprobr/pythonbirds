class Pessoa:
    def __init__(self,nome=None,idade=35):
        self.nome =nome
        self.idade = idade
        
    def cumprimetar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimetar(p))
    print(id(p))
    print(p.cumprimetar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)


