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
        return f'Olá {id(self)}'

if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro Soares Santos')
    # Passo o atributo de filhos e o atributo nomeado
    hernany = Pessoa(pedro, nome='Hernany Santos')
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
    print(id(Pessoa.olhos)), id(hernany.olhos), id(pedro.olhos))
