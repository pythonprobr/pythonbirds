class Pessoa:
    def cumprimetar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimetar(p))
    print(id(p))
    print(p.cumprimetar())


