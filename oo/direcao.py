class Direcao:
    # Responsabilidade de controlar a direção
    def __init__(self):
        self.valor = 'Norte'
        self.posicao = 0
        self.direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']


    def mostra_direcao(self):
        return self.direcoes[self.posicao]
    
    def direita(self):
        self.posicao += 1
        if self.posicao <= 3:
            self.valor = self.direcoes[self.posicao]
        else:
            self.posicao = 0
            self.valor = self.direcoes[self.posicao]

        return self.valor

    def esquerda(self):
        self.posicao -= 1
        if self.posicao >= 0:
            self.valor = self.direcoes[self.posicao]
        else:
            self.posicao = len(self.direcoes) - 1
            self.valor = self.direcoes[self.posicao]

        return self.valor
