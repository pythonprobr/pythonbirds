from atores import ATIVO


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter


class Fase():
    def __init__(self):
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

    def adicionar_obstaculo(self, *obstaculos):
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        self._passaros.extend(passaros)

    def acabou(self, tempo):
        return not self._existe_porco_ativo(tempo) or not self._existe_passaro_ativo(tempo)

    def status(self, tempo):
        if self._existe_passaro_ativo(tempo):
            return 'Jogo em andamento.'
        if self._existe_porco_ativo(tempo):
            return 'Jogo em encerrado. Você perdeu!'
        return 'Jogo em encerrado. Você ganhou!'

    def lancar(self, angulo, tempo):
        for passaro in self._passaros:
            if not passaro.foi_lancado():
                passaro.lancar(angulo, tempo)
                return

    def _existe_porco_ativo(self, tempo):
        return self._verificar_se_existe_ator_ativo(self._porcos, tempo)

    def _verificar_se_existe_ator_ativo(self, atores, tempo):
        for a in atores:
            if a.status(tempo) == ATIVO:
                return True
        return False

    def _existe_passaro_ativo(self, tempo):
        return self._verificar_se_existe_ator_ativo(self._passaros, tempo)


