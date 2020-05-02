class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=63):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    jairo = Pessoa(nome='Jairo')
    maria  = Pessoa(jairo, nome='Maria')
    print(Pessoa.cumprimentar(maria))
    print(id(maria))
    print(maria.cumprimentar())
    print(maria.nome)
    print(maria.idade)
    for filho in maria.filhos:
        print(filho.nome)
    maria.sobrenome = 'Almeida'
    #maria.sobrenome
    del maria.filhos
    maria.olhos=1
    del maria.olhos
    print(maria.nome, maria.sobrenome)
    print(jairo.__dict__)
    print(maria.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(maria.olhos)
    print(jairo.olhos)
    print(id(Pessoa.olhos), id(jairo.olhos), id(maria.olhos))