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
    def __init__(self, nome=None , idade = 45): #Nome nesssa opção é um parametro da função
        self.idade = idade
        self.nome = nome # Definindo um atriburo com vaor nulo, nesse caso o self.nome é um atributo
                            # da função.
        
    def cumprimentar(self):
        return f'Olá '
    
if __name__ == '__main__':
    p = Pessoas('Alex')
    # Opçào 1 para imprimir um objeto
    print('Uma opção para imprimir o objeto')
    print(Pessoas.cumprimentar(p))
    # Opção 2 para imprimir um objeto , sendo esse o mais pratico e usual.
    print('Outra opção para imprimir o objeto')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
