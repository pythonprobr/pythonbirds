'''

Você deve criar uma classe carro que via possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade;
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decemntar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela
oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste;
2) Método girar_a_direita
3) Método girar_a_esquerda


      >>>carro = Motor()
      >>>carro.acelerar
      >>>carro.calcular_velocidade
      1
      >>>carro.acelerar
      >>>carro.calcular_velocidade
      2
'''

class Carro:
    def __init__(self):
        pass
    pass

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade-=2
        self.velocidade=max(0, self.velocidade)

class Direção:
    pass



if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar
    print(motor.acelerar)
    print(motor.velocidade)