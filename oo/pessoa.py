class Pessoa:
    def __init__(self, nome = None, idade = None, altura = None):
        self.altura = altura
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Ola, tudo certo contigo bro?'

if __name__ == '__main__':
    p = Pessoa('Junio')
    print(p.nome)
    print(p.cumprimentar())
    print(type(p))
    p.nome = 'Henrique'
    print(p.nome)
