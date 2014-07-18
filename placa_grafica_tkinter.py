# coding: utf-8
import time
from tkinter import PhotoImage, NW, Tk, Canvas
from tkinter.constants import ALL

from fase import Fase
from atores import PassaroVermelho, PassaroAmarelo, Porco, Obstaculo


def get_angulo(event):
    global angulo_input, popup_angulo
    print(angulo_input.get())
    popup_angulo.destroy()


ALTURA_DA_TELA = 600  # px





# popup_angulo = Toplevel(root)
# Label(popup_angulo, text="Digite o angulo de lançamento: ").pack()
# angulo_input = Entry(popup_angulo)
# angulo_input.pack(padx=6)
# b = Button(popup_angulo, text="OK", command=get_angulo)
# b.pack(pady=5)

root = Tk()

PASSARO_VERMELHO = PhotoImage(file="images/passaro_vermelho.gif")
PASSARO_AMARELHO = PhotoImage(file="images/passaro_amarelo.gif")
PORCO = PhotoImage(file="images/porco.gif")
PORCO_MORTO = PhotoImage(file="images/porco_morto.gif")
OBSTACULO = PhotoImage(file="images/obstaculo.gif")
TRANSPARENTE = PhotoImage(file="images/transparente.gif")
BACKGROUND = PhotoImage(file="images/background.gif")

CARACTER_PARA__IMG_DCT = {'D': PASSARO_VERMELHO, '>': PASSARO_AMARELHO, '@': PORCO, 'O': OBSTACULO,
                          '+': PORCO_MORTO, ' ': TRANSPARENTE}


def plotar(camada_de_atores, ponto):
    multiplicador = 10  # 10 px/m
    x = multiplicador * ponto.x
    y = ALTURA_DA_TELA - ponto.y * multiplicador - 12 * multiplicador
    image = CARACTER_PARA__IMG_DCT.get(ponto.caracter, TRANSPARENTE)
    camada_de_atores.create_image((x, y), image=image, anchor=NW)
    # camada_de_atores.create_rectangle(x, y, 150, 75, fill="blue")


def animar(tela, camada_de_atores, fase, passo=0.1, delta_t=0.1):
    tempo = 0
    passo = int(1000 * passo)

    def _animar():
        camada_de_atores.delete(ALL)
        camada_de_atores.create_image((0, 0), image=BACKGROUND, anchor=NW)
        nonlocal tempo
        tempo += delta_t
        for ponto in fase.calcular_pontos(tempo):
            plotar(camada_de_atores, ponto)
        tela.after(passo, _animar)

    camada_de_atores.pack()
    _animar()
    tela.mainloop()

    tela.after(passo, _animar)


if __name__ == '__main__':
    root.title("Python Birds")
    root.geometry("800x600")
    root.resizable(0, 0)

    stage = Canvas(root, width=800, height=ALTURA_DA_TELA)

    fase = Fase()
    passaros = [PassaroVermelho(3, 3), PassaroAmarelo(3, 3), PassaroAmarelo(3, 3)]
    porcos = [Porco(75, 1), Porco(70, 1)]
    obstaculos = [Obstaculo(31, 10)]

    fase.adicionar_passaro(*passaros)
    fase.adicionar_porco(*porcos)
    fase.adicionar_obstaculo(*obstaculos)

    fase.lancar(45, 1)
    fase.lancar(63.5, 2)
    fase.lancar(23, 3)

    animar(root, stage, fase)

    # root.wait_window(popup_angulo)
