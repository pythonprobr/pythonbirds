# Trabalhando com atributos default ou de classe
class Pessoa:
    # Atributo default ou classe
    olhos = 2 # Valor default para o atributo da classe
    # Executado quanto é construída a classe(Atributos de Instância)
    def __init__(self, *filhos, nome=None, idade=39):
        # Atributos da Classe
        self.idade = idade
        self.nome = nome
        # Atributos complexos : Listas, Dicionários, Tuplas
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é: {self.nome}'
    
    # Métodos da Classe.... Utiliza-se decorations
    @staticmethod
    def metodo_estatico():
        return 42

    # Tem acesso aos atributos da classe
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

#Herança - Herda de Pessoa
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai=super().cumprimentar()
        return f'{cumprimentar_da_classe_pai} Aperto de mão'

class Mutante(Pessoa):
    # Sobrescrita de atributo
    olhos = 3

if __name__ == '__main__':
    rosinha = Mutante(nome='Rosilaine')
    pedro = Homem(nome='Pedro')
    # Passo o atributo de filhos e o atributo nomeado
    hernany = Homem(pedro, nome='Hernany Santos')
    print(Pessoa.cumprimentar(hernany))
    print(id(hernany))
    print(hernany.cumprimentar())
    print(hernany.nome)
    print(hernany.idade)
    for filho in hernany.filhos:
        print(filho.nome)
    
    # Atributos Dinâmicos - Criados em tempos de execução
    hernany.sobrenome = 'Santos'
    # Remove atributos dinâmicos ou não
    del hernany.filhos
    hernany.olhos = 1
    del hernany.olhos
    '''
     __dict__ Verifica os atributos que compoe o objeto, mostrando os de tempo de execução(Atributos de Instância) ou que estão declarados na classe
     Os atributos de instância nos dá uma licença poética para acrescentar um campo necessário para um determinado momento.
     Não deve-se usar deste recurso repetidas vezes pois a utilização deste pode causar dificuldade de entendimento do código para terceiros, além
     de não ser uma boa prática
    '''
    print(hernany.__dict__)
    print(pedro.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(hernany.olhos)
    print(pedro.olhos)
    print(id(Pessoa.olhos), id(hernany.olhos), id(pedro.olhos))
    print(Pessoa.metodo_estatico(), hernany.metodo_estatico()) #42
    print(Pessoa.nome_e_atributos_de_classe(), hernany.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    # Verifica se objeto é de determinada classe
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(pedro, Pessoa))
    print(isinstance(pedro, Homem))
    print(rosinha.olhos)
