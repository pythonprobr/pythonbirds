class Pessoa:
    def __init__(self, *filhos, nome = None, idade = None, altura = None):
        self.altura = altura
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def __str__(self):
        return f'{self.filhos}'

    def cumprimentar(self):
        return 'Ola, tudo certo contigo bro?'

if __name__ == '__main__':
    seiya = Pessoa(nome = 'Seiya')
    amanda = Pessoa(nome = 'Amanda')
    tohka = Pessoa(nome = 'Tohka')
    henrique = Pessoa(seiya, amanda, tohka, nome = 'Henrique')
    print(henrique.nome)
    print(f'----Os filhos de {henrique.nome} são:')
    for filhos in henrique.filhos:
        print(f'--------{filhos.nome}--------')

