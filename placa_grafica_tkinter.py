# coding: utf-8
import time
from tkinter import PhotoImage, NW, Tk, Canvas
from tkinter.constants import ALL
import math
from os import path
import atores

from fase import Fase, EM_ANDAMENTO, VITORIA
from atores import PassaroVermelho, PassaroAmarelo, Porco, Obstaculo

ALTURA_DA_TELA = 600  # px

root = Tk()

IMAGES_PATH = path.dirname(__file__)
IMAGES_PATH = path.join(IMAGES_PATH, 'images')
PASSARO_VERMELHO = PhotoImage(file=path.join(IMAGES_PATH, "passaro_vermelho.gif"))
PASSARO_AMARELHO = PhotoImage(file=path.join(IMAGES_PATH, "passaro_amarelo.gif"))
PORCO = PhotoImage(file=path.join(IMAGES_PATH, "porco.gif"))
PORCO_MORTO = PhotoImage(file=path.join(IMAGES_PATH, "porco_morto.gif"))
OBSTACULO = PhotoImage(file=path.join(IMAGES_PATH, "obstaculo.gif"))
TRANSPARENTE = PhotoImage(file=path.join(IMAGES_PATH, "transparente.gif"))
BACKGROUND = PhotoImage(file=path.join(IMAGES_PATH, "background.gif"))
PYTHONBIRDS_LOGO = PhotoImage(file=path.join(IMAGES_PATH, "python-birds-logo.gif"))
MENU = PhotoImage(file=path.join(IMAGES_PATH, "menu.gif"))
VOCE_GANHOU = PhotoImage(file=path.join(IMAGES_PATH, "python-birds-voce-ganhou-popup.gif"))
VOCE_PERDEU = PhotoImage(file=path.join(IMAGES_PATH, "python-birds-voce-perdeu-popup.gif"))

CARACTER_PARA__IMG_DCT = {'V': PASSARO_VERMELHO,
                          'A': PASSARO_AMARELHO,
                          '@': PORCO,
                          'O': OBSTACULO,
                          '+': PORCO_MORTO,
                          ' ': TRANSPARENTE}


def plotar(camada_de_atores, ponto):
    if ponto.caracter != ' ':
        x = ponto.x
        y = ALTURA_DA_TELA - ponto.y - 120  # para coincidir com o chao da tela
        image = CARACTER_PARA__IMG_DCT.get(ponto.caracter, TRANSPARENTE)
        camada_de_atores.create_image((x, y), image=image, anchor=NW)


def animar(tela, camada_de_atores, fase, passo=0.01, delta_t=0.04):
    tempo = 0
    passo = int(1000 * passo)
    angulo = 0
    multiplicador_rebobinar = 20

    def _animar():
        tempo_de_inicio_de_animacao=time.time()

        nonlocal tempo
        nonlocal delta_t
        nonlocal angulo
        tempo += delta_t
        if tempo <= 0:
            tempo = 0
            delta_t /= -multiplicador_rebobinar
        if fase.status() != EM_ANDAMENTO:
            camada_de_atores.create_image(162, 55, image=PYTHONBIRDS_LOGO, anchor=NW)
            camada_de_atores.create_image(54, 540, image=MENU, anchor=NW)
            if fase.status() == VITORIA:
                img = VOCE_GANHOU
            else:
                img = VOCE_PERDEU
            camada_de_atores.create_image(192, 211, image=img, anchor=NW)
        else:
            camada_de_atores.delete(ALL)
            camada_de_atores.create_image((0, 0), image=BACKGROUND, anchor=NW)
            tamanho_seta = 60
            angulo_rad = math.radians(-angulo)

            camada_de_atores.create_line(52, 493, 52 + tamanho_seta * math.cos(angulo_rad),
                                         493 + tamanho_seta * math.sin(angulo_rad), width=1.5)
            camada_de_atores.create_text(35, 493, text="%d°" % angulo)
            for ponto in fase.calcular_pontos(tempo):
                plotar(camada_de_atores, ponto)
            tempo_gasto_com_animacao= round((time.time() - tempo_de_inicio_de_animacao)*1000) # Trans
            tempo_proxima_animacao = passo - tempo_gasto_com_animacao if passo>tempo_gasto_com_animacao else 1
            tela.after(tempo_proxima_animacao, _animar)

    def _ouvir_comandos_lancamento(evento):
        nonlocal angulo
        if evento.keysym == 'Up':
            angulo += 1
            if angulo > 360:
                angulo = 1
        elif evento.keysym == 'Down':
            angulo -= 1
            if angulo < 0:
                angulo = 359
        elif evento.keysym == 'Return' or evento.keysym == 'space':
            fase.lancar(angulo, tempo)

    def _replay(event):
        return
        nonlocal tempo
        nonlocal delta_t
        if fase.acabou(tempo):
            delta_t *= -multiplicador_rebobinar
            _animar()


    def _jogar_novamente(event):
        return
        nonlocal tempo
        nonlocal delta_t
        if fase.acabou(tempo):
            tempo = delta_t
            fase.resetar()
            _animar()

    def _finalizar(event):
        root.destroy()

    camada_de_atores.pack()
    _animar()
    tela.bind_all('<KeyPress>', _ouvir_comandos_lancamento)
    tela.bind_all('1', _replay)
    tela.bind_all('2', _jogar_novamente)
    tela.bind_all('3', _finalizar)
    tela.bind_all('<Escape>', _finalizar)

    tela.mainloop()
    tela.after(passo, _animar)


def rodar_fase(fase):
    root.title("Python Birds")
    root.geometry("800x600")
    root.resizable(0, 0)
    stage = Canvas(root, width=800, height=ALTURA_DA_TELA)

    multiplicador = 10
    PassaroAmarelo.velocidade_escalar *= multiplicador
    PassaroVermelho.velocidade_escalar *= multiplicador
    atores.GRAVIDADE = 100
    animar(root, stage, fase)


if __name__ == '__main__':
    fase = Fase(intervalo_de_colisao=32)
    passaros = [PassaroVermelho(30, 30), PassaroAmarelo(30, 30), PassaroAmarelo(30, 30)]
    porcos = [Porco(750, 1), Porco(700, 1)]
    obstaculos = [Obstaculo(310, 100)]

    fase.adicionar_obstaculo(*obstaculos)
    fase.adicionar_passaro(*passaros)
    fase.adicionar_porco(*porcos)
    rodar_fase(fase)
