# -*- coding: utf-8 -*-
from itertools import chain
from tkinter import PhotoImage, NW
from atores import ATIVO
from fase import Ponto, Fase

PASSARO_VERMELHO = "images/passaro_vermelho.gif"
PASSARO_AMARELHO = "images/passaro_amarelo.gif"
PORCO = "images/porco.gif"
PORCO_MORTO = "images/porco_morto.gif"
OBSTACULO = "images/obstaculo.gif"
TRANSPARENTE = "images/transparente.gif"

CARACTER_PARA_CAMINHO_IMG_DCT = {'D': PASSARO_VERMELHO, '>': PASSARO_AMARELHO, '@': PORCO, 'O': OBSTACULO,
                                 '+': PORCO_MORTO}

caracter_para_img = {}


def get_imagem(caracter):
    # img = caracter_para_img.get(caracter)
    # if img is None:
    #     caracter_para_img[caracter] = PhotoImage(file=CARACTER_PARA_CAMINHO_IMG_DCT.get(caracter, TRANSPARENTE))
    return PhotoImage(file=CARACTER_PARA_CAMINHO_IMG_DCT.get(caracter, TRANSPARENTE))
    # return img


def ator_para_cooredenadas(ator):
    return ator.x, ator.y


def criar_imagem(canvas, ator):
    imagem = get_imagem(ator.caracter(0))
    return imagem, canvas.create_image(ator_para_cooredenadas(ator),
                                       image=imagem,
                                       anchor=NW)


class FaseTk(Fase):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas

    def _adicionar_ator(self, lista, *atores):
        super()._adicionar_ator(lista, *atores)
        for ator in atores:
            ator.img, ator.img_id = criar_imagem(self.canvas, ator)

    def _transformar_em_ponto(self, ator, tempo):
        ponto = super()._transformar_em_ponto(ator, tempo)
        ponto.canvas_img = ator.img
        ponto.canvas_img_id = ator.img_id
        ponto.new_photo_img = get_imagem(ponto.caracter)
        return ponto

