class Pessoa:
    def cumprimetar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimetar(p))
    print(id(p))
    print(p.cumprimetar())
