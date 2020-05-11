class Motor:
    # Responsabilidade de controlar a velocidade
   velocidade = 0

   @classmethod
   def acelerar(cls):
       cls.velocidade += 1
       return cls.velocidade

   @classmethod
   def frear(cls):
       cls.velocidade -= 2
       if cls.velocidade < 0:
           cls.velocidade = 0
       return cls.velocidade

class Direcao:
    # Responsabilidade de controlar a direção
    valor = 'Norte'
    posicao = 0
    direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']

    @classmethod
    def mostra_direcao(cls):
        return cls.direcoes[cls.posicao]
    
    @classmethod
    def girar_a_direita(cls):
        cls.posicao += 1
        if cls.posicao <= 3:
            cls.valor = cls.direcoes[cls.posicao]
        else:
            cls.posicao = 0
            cls.valor = cls.direcoes[cls.posicao]

        return cls.valor

    @classmethod
    def girar_a_esquerda(cls):
        cls.posicao -= 1
        if cls.posicao >= 0:
            cls.valor = cls.direcoes[cls.posicao]
        else:
            cls.posicao = len(cls.direcoes) - 1
            cls.valor = cls.direcoes[cls.posicao]

        return cls.valor


class Carro:
    motor = Motor()
    direcao = Direcao()


if __name__ == '__main__':
    carro = Carro()
    print('Testando o Motor')
    print(carro.motor.velocidade)
    print(carro.motor.acelerar())
    print(carro.motor.acelerar())
    print(carro.motor.acelerar())
    print(carro.motor.frear())
    print(carro.motor.frear())
    print('Testando a Direção')
    print(carro.direcao.valor)
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_direita())
    print(carro.direcao.girar_a_esquerda())
    print(carro.direcao.girar_a_esquerda())
