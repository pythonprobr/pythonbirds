class Pessoa:
    olhos  = 2
    def __init__(self,*filhos,nome=None,idade=35):
        self.nome =nome
        self.idade = idade
        self.filhos = list(filhos)
        
    def cumprimetar(self):
        return f'Ola {id(self)} = {self.nome}'
    
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homen(Pessoa):
    pass

if __name__ == '__main__':
    renzo = Homen(nome='Renzo')
    luciano = Pessoa(renzo,nome='Luciano')
    
    print(Pessoa.cumprimetar(luciano))
    print(id(luciano))
    print(luciano.cumprimetar())
    print(luciano.nome)
    print(luciano.idade)
    
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = "Ramalho"
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())


#
#99999
