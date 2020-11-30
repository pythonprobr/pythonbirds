class Pessoa:

    olhos = 2                                               #Utilizado para criar atributos de classe, quando o valor é igual para todos os objetos

    def __init__(self, *filhos, nome=None, idade=35):       #utilizado para criar atributos de classe
        self.idade = idade
        self.nome = nome
        self.filhos= list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'




    @staticmethod                                   #utilizado para acessar um metodo que independe do objeto wue esta sendo executado
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):            #utilizado para acessar dados da mesma classe
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':       #utilizado para realizar o teste
    renzo = mutante(nome='Renzo')
    luciano = Homem(renzo, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'   #permite criar atributos dinamicos
    del luciano.filhos              #permite remover um atributo
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())

