class Pessoa():
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joaozinho = Pessoa(nome='Joãozinho')
    joao = Pessoa(joaozinho, nome='João')
    print(Pessoa.cumprimentar(joao))
    print(id(joao))
    print(joao.cumprimentar())
    print(joao.nome)
    print(joao.idade)
    for filho in joao.filhos:
        print(f'filho {filho.nome}')

#Criando atributo em tempo de execução para o objeto específico específico
    joao.sobrenome = 'Santos'
    print(joao.__dict__) # O __dict__ mostra os atributos, o sobrenome so tem em João
    print(joaozinho.__dict__)

#Deletando filhos do objeto João
    del joao.filhos
    print(joao.__dict__)