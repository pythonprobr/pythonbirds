class Pessoa:
    # Executado quanto é construída a classe
    def __init__(self, nome=None, idade=39):
        # Atributos da Classe
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Hernany')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Santos'
    print(p.nome)
    print(p.idade)