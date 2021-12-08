class Pessoa:
    def __init__(self,*filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimetar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    josevaldo = Pessoa(nome='Josevaldo')
    joviniano = Pessoa(josevaldo, nome='Joviniano')
    print(Pessoa.cumprimetar(joviniano))
    print(id(joviniano))
    print(joviniano.cumprimetar())
    print(joviniano.nome)
    print(joviniano.idade)
    for filho in joviniano.filhos:
        print(filho.nome)
joviniano.sobrenome = 'Pereira'
del joviniano.filhos
print(joviniano.__dict__)
print(josevaldo.__dict__)
