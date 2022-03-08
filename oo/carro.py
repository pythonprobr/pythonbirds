"""
Criar um carro pela composição a partir de duas classes
1)Motor
2)Direção

O motor terá que controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dados Velocidade
2) Metodo Acelerar, que deverar incrementar 1 velocidade em 1 unidade
3) Método de frear que devera decrementar 2 velocidades

A direção deve controlar a direção
1)Valor de direção é Norte, sul, leste e oeste
2)Metodo girar_a_direita e girar_a_esquerda
3)Método frear que deverá decrementar a velocidade em duas unidades
A direção terá a responsabilidade de controlar a diração.
Ela oferece os seguinter atributos:

A direção terá a responsabilidade de controlar a derição. Ela
oferece os seguintes atributos:
1) Valor de direção com valores possíveis : Norte, Sul, Leste e Oeste.
2)Método girar_a_direita
3)Método girar_a_esquerda

    N
    
O       L

    S
    
    Exemplo:
    >>> # Testando Motor
    >>> motor.Motor()
    >>> motor.velocidade
    0
    >>>motor.acelerar()
    >>>motor.velocidade
    1
    >>>motor.acelerar()
    >>>motor.velocidade
    2
    >>>motor.acelerar()
    >>>motor.velocidade
    3
    >>>motor.frear()
    >>>motor.velocidade
    1
    >>>motor.frear()
    >>>motor.velocidade
    0
    >>> # Testando Direcao
    >>>direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>>direcao.girar_a_direita()
    >>>direcao.valor
    'Leste'
    >>>direcao.girar_a_direita()
    >>>direcao.valor
    'Sul'
    >>>direcao.girar_a_direita()
    >>>direcao.valor
    'Oeste'
    >>>direcao.girar_a_direita()
    >>>direcao.valor
    'Norte'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor
    'Oeste'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor
    'Sul'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor
    'Leste'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor
    'Norte'
    >>> carro = Carro(direcao,motor)
    >>> carro.calcular_velocidade()
    0
    >>>motor.acelerar()
    >>>motor.velocidade
    1
    >>>motor.acelerar()
    >>>motor.velocidade
    2
     >>>motor.frear()
    >>>motor.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>>'Norte'
    >>>carro.girar_a_direita()
    >>>carro.calcular_direcao()
    >>>'Leste'
    >>>carro.girar_a_esquerda()
    >>>carro.calcular_diracao()
    >>>'Norte'
    >>>carro.girar_a_esquerda()
    >>>carro.girar_a_esquerda()
    >>>'Oeste'
"""
class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar (self):
        self.acelerar +=1
    def frear(self):
        self.frear -=2
