class Pessoa:
    # Executado quanto é construída a classe
    def __init__(self, *filhos, nome=None, idade=39):
        # Atributos da Classe
        self.idade = idade
        self.nome = nome
        # Atributos complexos : Listas, Dicionários, Tuplas
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro Soares Santos')
    # Passo o atributo de filhos e o atributo nomeado
    hernany = Pessoa(pedro, nome='Hernany Santos')
    print(Pessoa.cumprimentar(hernany))
    print(id(hernany))
    print(hernany.cumprimentar())
    print(hernany.nome)
    print(hernany.idade)
    for filho in hernany.filhos:
        print(filho.nome)