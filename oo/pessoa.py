class Pessoa:
    olhos = 2 

    def __init__(self, *filhos, nome = None, idade = 24):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
        

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls}- olhos {cls.olhos}'

if __name__ == '__main__':
    joao = Pessoa(nome = 'João')
    alefe = Pessoa(joao, nome = 'Alefe')
    print(Pessoa.cumprimentar(alefe))
    print(id(alefe))
    print(alefe.cumprimentar())
    print(alefe.nome)
    print(alefe.idade)
    for filho in alefe.filhos:
        print(filho.nome)
    print(alefe.filhos)
    alefe.sobrenome = 'Gomes'
    del alefe.filhos
    alefe.olhos = 1
    del alefe.olhos
    print(alefe.__dict__)
    print(joao.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(joao.olhos)
    print(alefe.olhos)
    print(id(Pessoa.olhos), id(joao.olhos), id(alefe.olhos))
    print(Pessoa.metodo_estatico(), alefe.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),alefe.nome_e_atributos_de_classe())
    

 


 # Se o valor do atributo for o mesmo de todos objetos ele deve ser um atributo de classe
 # Se for diferente, ele deve ser criado como atributo de instancia