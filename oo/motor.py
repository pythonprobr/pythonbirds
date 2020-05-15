class Motor:
    # Responsabilidade de controlar a velocidade
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
       self.velocidade += 1
       return self.velocidade

    def frear(self):
       self.velocidade -= 2
       if self.velocidade < 0:
           self.velocidade = 0
       return self.velocidade