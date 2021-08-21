class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 24):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joao = Pessoa(nome = 'João')
    alefe = Pessoa(joao, nome = 'Alefe')
    print(Pessoa.cumprimentar(alefe))
    print(id(alefe))
    print(alefe.cumprimentar())
    print(alefe.nome)
    print(alefe.idade)
    for filho in alefe.filhos:
        print(filho.nome)
    print(alefe.filhos)
    alefe.sobrenome = 'Gomes'
    del alefe.filhos
    print(alefe.__dict__)
    print(joao.__dict__)
    