# Crianda a classe pessoa
class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(id(p))
    print(p.cumprimentar())