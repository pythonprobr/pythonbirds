class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

    def __str__(self):
        return f"Sr(a) {self.nome}"


if __name__ == '__main__':
    p = Pessoa(nome='Marcos', idade=45)
    pessoa_filho = [Pessoa(nome='Layla', idade=21), Pessoa(nome='Isabel', idade=19)]
    print(Pessoa.cumprimentar(p))
    for filho in pessoa_filho:
        print(f" filho de {p}: {filho.nome}, {filho.idade}")

    print(p, p.idade)
