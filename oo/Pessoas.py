"""
Exemplo de como deve ser criado uma class em Python
As classes devem sempre começar com a primeira letra em Maiusculo ,
  caso seja uma palavra composta a primeira letra de cada palavra
  deve iniciar em Maiusculo.
  Ex.: De classes
        class FrutasCitricas:
            pass - Essa opção é usada para deixar uma classe funcional
                   e temporareamene sem dados.
        
        class Fturas:
            pass
"""

class Pessoas:
    olhos = 2 #Atributo de classe , atributo que é vinculado a lasse e não somente ao objeto
    def __init__(self, *filhos, nome=None , idade = 45): #Nome nesssa opção é um parametro da função
        self.idade = idade
        self.nome = nome # Definindo um atriburo com vaor nulo, nesse caso o self.nome é um atributo
                            # da função.
        self.filhos = list(filhos) # Lista como parametros com permissão de um pra muitos,
                                # Um pais para muitos filhos e nunca um fiho pra muitos pais.
        
    def cumprimentar(self):
        return f'Olá '
    
    #Metodo de classe
    @staticmethod # Decoreitos  - São inicados com o @
    def metodo_statico():
        return 42 # Usado para fazer algum calculo independente da classe e do objeto
    
    @classmethod # Metodo de acesso a cvlasse que esta execultando o metodo
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
 
#Classe homem erdando da classe Pessoa.
class Homem(Pessoas):
    pass
 
"""
Neste exemplo de filhos esta sendo utilizando os nome ficticios de João
 e Jose - Sendo Joào o pai de José
"""
if __name__ == '__main__':
    _jose = Pessoas(nome='José')
    _joao = Pessoas(_jose, nome='João')
    # Opção 1 para imprimir um objeto , sendo esse o mais pratico e usual.
   # print('Outra opção para imprimir o objeto')
   # print(_joao.cumprimentar())
   # print(_joao.nome)
   # print(_joao.idade)
    print()
    for filho in _joao.filhos:
        print(f'{_joao.cumprimentar()},{_joao.nome} como esta seu filho {filho.nome} ?')
    _joao.sobrenome = 'Santos' #Atributo dinamico, criado apenas para esse objeto e essa rotina
    del _joao.filhos # Usando a palavra reservada DEL para apagar o atributo dinamio sobrenome
    _joao.olhos = 3
    print(_joao.olhos)
    print(_joao.__dict__ )
    print(_jose.__dict__)
    print(Pessoas.olhos)
    print(Pessoas.metodo_statico(), _joao.metodo_statico())
    print(Pessoas.nome_e_atributos_de_classe(), _jose.nome_e_atributos_de_classe())
 # Opçào 2 para imprimir um objeto
  #  print('Uma opção para imprimir o objeto')
  #  print(Pessoas.cumprimentar(p))