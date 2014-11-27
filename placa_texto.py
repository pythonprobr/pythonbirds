# -*- coding: utf-8 -*-
import os
import platform
import time
import sys
from templates import FIM

try:
    import msvcrt
except:
    pass
import select


eh_windows = platform.system() == 'Windows'
apagar_tela = lambda: os.system('cls') if eh_windows else lambda: os.system('clear')

# workaround retirado de http://stackoverflow.com/questions/292095/polling-the-keyboard-in-python


def ouvir_teclado_fn():
    i, o, e = select.select([sys.stdin], [], [], 0.0001)
    for s in i:
        if s == sys.stdin:
            return True
    return False


if eh_windows:
    ouvir_teclado = msvcrt.kbhit
else:
    ouvir_teclado = ouvir_teclado_fn

LARGURA = 80
ALTURA = 20


def desenhar_e_esperar(delta_t, fase, passo, tempo, msg):
    time.sleep(passo)
    pontos_cartesianos = fase.calcular_pontos(tempo)
    print()
    print('############### %s Tempo: %.2f #################' % (msg, tempo))
    print(desenhar(*pontos_cartesianos))
    tempo += delta_t
    return tempo


def _animar(delta_t, fase, passo, tempo, msg):
    while not fase.acabou(tempo):
        tempo = desenhar_e_esperar(delta_t, fase, passo, tempo, msg)
    return tempo


def _jogar(delta_t, fase, passo, tempo, msg):
    while not fase.acabou(tempo):
        tempo = desenhar_e_esperar(delta_t, fase, passo, tempo, msg)
        entrada = ouvir_teclado()
        if entrada:
            while True:
                try:
                    if not eh_windows:
                        input()
                    angulo = float(input('Digite o Ângulo de Lançamento: '))
                    fase.lancar(angulo, tempo)
                    break
                except:
                    print('Erro: valor tem que ser númerico!')
    return tempo


def rebobina(delta_t, fase, passo, tempo, msg):
    while tempo > 0:
        tempo = desenhar_e_esperar(-delta_t, fase, passo, tempo, msg)
    return tempo


def animar(fase, passo=0.1, delta_t=0.1):
    tempo = 0
    tempo_final = _jogar(delta_t, fase, passo, tempo, 'Play!')
    if input('Deseja ver o Replay? (s para sim): ').lower() == 's':
        velocidade_rebobina = 10
        rebobina(delta_t, fase, passo / velocidade_rebobina, tempo_final,
                 'Rebobinando %s vezes mais rápido!' % velocidade_rebobina)
        velocidade_replay = 1
        _animar(delta_t, fase, passo / velocidade_replay, tempo, 'Replay %s vezes mais rápido!' % velocidade_replay)
    apagar_tela()
    print(fase.status(tempo_final))
    print(FIM)


def normalizar_coordenadas(x, y):
    return x, ALTURA - y - 1


def esta_dentro_da_tela(x, y):
    return 0 < x < (LARGURA - 1) and 0 < y < (ALTURA - 1)


def escolher_caracter_limitrofe(x, y):
    if x == 0 or x == LARGURA - 1:
        return '|'
    if y == 0:
        return '-'
    return 'T'


def escolher_caracter(x, y, *pontos_cartesianos):
    for ponto in pontos_cartesianos:
        x_normalizdo, y_normalizado = normalizar_coordenadas(ponto.x, ponto.y)
        if x == x_normalizdo and y == y_normalizado:
            return ponto.caracter
    return ' '


def desenhar(*pontos_cartesianos):
    return [p for p in pontos_cartesianos]


def main():
    from atores import PassaroVermelho, PassaroAmarelo, Porco, Obstaculo
    from fase import Fase

    fase_exemplo = Fase()
    passaros = [PassaroVermelho(3, 3), PassaroAmarelo(3, 3), PassaroAmarelo(3, 3)]
    porcos = [Porco(78, 1), Porco(70, 1)]
    obstaculos = [Obstaculo(31, 10)]

    fase_exemplo.adicionar_passaro(*passaros)
    fase_exemplo.adicionar_porco(*porcos)
    fase_exemplo.adicionar_obstaculo(*obstaculos)

    # Solução para ganhar
    # fase_exemplo.lancar(45, 1)
    # fase_exemplo.lancar(63, 3)
    # fase_exemplo.lancar(23, 4)

    animar(fase_exemplo)


if __name__ == '__main__':
    main()
