class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá {id(self)}"


if __name__ == '__main__':
    p = Pessoa(nome='marcos', idade=45)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome, p.idade)
