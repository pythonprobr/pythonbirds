class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None, sobrenome=None):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

    def __str__(self):
        return f"Sr(a) {self.nome}"


if __name__ == '__main__':
    p = Pessoa(nome='Marcos', idade=45, sobrenome='Viana')
    pessoa_filho = [Pessoa(nome='Layla', idade=21, sobrenome=p.sobrenome), Pessoa(nome='Isabel', idade=19, sobrenome=p.sobrenome)]
    print(Pessoa.cumprimentar(p))
    p.filhos = pessoa_filho
    p.mid_nome = 'Paulo'
    print(p.__dict__)

    del p.mid_nome
    print(p.__dict__)
    for filho in pessoa_filho:
        print(f" filho de {p}: {filho.nome} {filho.sobrenome}, {filho.idade}")

    print(p, p.idade)
