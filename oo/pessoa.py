class Pessoa:
    def cumprimentar(self):
        return 'Ola, tudo certo contigo bro?'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(type(p))
