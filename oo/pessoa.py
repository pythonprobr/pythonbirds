class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimetar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_statico():
        return 42
    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
class Homem(Pessoa):
    def cumprimetar(self):
        cumprimentar_da_classe=super().cumprimetar()
        return f'{cumprimentar_da_classe}.Aperto de mão!'


class Mutante(Pessoa):
    olhos =  3

if __name__ == '__main__':
    josevaldo = Mutante(nome='Josevaldo')
    joviniano = Homem(josevaldo, nome='Joviniano')
    print(Pessoa.cumprimetar(joviniano))
    print(id(joviniano))
    print(joviniano.cumprimetar())
    print(joviniano.nome)
    print(joviniano.idade)
    for filho in joviniano.filhos:
        print(filho.nome)
joviniano.sobrenome = 'Pereira'
del joviniano.filhos
joviniano.olhos =   1
del joviniano.olhos
print(joviniano.__dict__)
print(josevaldo.__dict__)
print(Pessoa.olhos)
print(joviniano.olhos)
print(josevaldo.olhos)
print(id(Pessoa.olhos)),print(id(joviniano.olhos)), print(id(josevaldo.olhos))
print(Pessoa.metodo_statico(), joviniano.metodo_statico())
print(Pessoa.nome_e_atributo_de_classe(), joviniano.nome_e_atributo_de_classe())
pessoa = Pessoa('Anonimo')
print(isinstance(pessoa, Homem))
print(isinstance(josevaldo, Homem))
print(isinstance(josevaldo, Pessoa))
print(josevaldo.olhos)
print(joviniano.cumprimetar())
print(josevaldo.cumprimetar())
