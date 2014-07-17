from atores import ATIVO


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

    def _existe_porco_ativo(self, tempo):
        return self._verificar_se_existe_ator_ativo(self._porcos, tempo)

    def _verificar_se_existe_ator_ativo(self, atores, tempo):
        for a in atores:
            if a.status(tempo) == ATIVO:
                return True
        return False

    def _existe_passaro_ativo(self, tempo):
        return self._verificar_se_existe_ator_ativo(self._passaros,tempo)
