class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':       #utilizado para realizar o teste
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

