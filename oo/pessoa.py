class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = None, altura = None):
        self.altura = altura
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def __str__(self):
        return f'{self.filhos}'

    def cumprimentar(self):
        return 'Ola, tudo certo contigo bro?'

    @staticmethod # Método estatico que independe o método da classe, não necessitando
    # depender de objeto algum para ser rodado

if __name__ == '__main__':
    seiya = Pessoa(nome = 'Seiya')
    amanda = Pessoa(nome = 'Amanda')
    tohka = Pessoa(nome = 'Tohka')
    henrique = Pessoa(seiya, amanda, tohka, nome = 'Henrique')
    print(henrique.nome)
    print(f'----Os filhos de {henrique.nome} são:')
    for filhos in henrique.filhos:
        print(f'--------{filhos.nome}--------')
    print(tohka.olhos)
    tohka.olhos = 4
    print(tohka.olhos)
    print(tohka.__dict__) #Instância __dict__ para descobrir os parâmetros e caracteristicas das classes
    print(henrique.__dict__)#Instância __dict__ para descobrir os parâmetros e caracteristicas das classes
    del tohka.olhos
    print(tohka.__dict__)#Instância __dict__ para descobrir os parâmetros e caracteristicas das classes
    tohka.sobrenome = 'Kurosaki'
    print(f'--------{tohka.nome} {tohka.sobrenome}--------')
