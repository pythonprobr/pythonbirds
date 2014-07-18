# coding: utf-8
import time

from tkinter import *
from tkinter import ttk
from fase import Fase
from atores import PassaroVermelho, PassaroAmarelo, Porco, Obstaculo
from fase_tkinter import FaseTk


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






def plotar(canvas, ponto):
    multiplicador = 10  # 10 px/m
    x = multiplicador * ponto.x
    y = ALTURA_DA_TELA - ponto.y * multiplicador - 11 * multiplicador
    canvas.coords(ponto.canvas_img_id, (x, y))


def animar(tela,fase,passo=0.1, delta_t=0.1):
    tempo=0
    def _animar():
        nonlocal tempo
        tempo += delta_t
        time.sleep(passo)
        for ponto in fase.calcular_pontos(tempo):
            plotar(fase.canvas, ponto)
        tela.after(1, _animar)



    tela.after(1, _animar)
    tela.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title("Python Birds")
    root.geometry("800x600")
    root.resizable(0, 0)

    stage = Canvas(root, width=800, height=ALTURA_DA_TELA)
    bg_image = PhotoImage(file="images/background.gif")
    stage.create_image((0, 0), image=bg_image, anchor=NW)
    stage.pack()
    fase = FaseTk(stage)
    passaros = [PassaroVermelho(3, 3), PassaroAmarelo(3, 3), PassaroAmarelo(3, 3)]
    porcos = [Porco(75, 1), Porco(70, 1)]
    obstaculos = [Obstaculo(31, 10)]

    fase.adicionar_passaro(*passaros)
    fase.adicionar_porco(*porcos)
    fase.adicionar_obstaculo(*obstaculos)

    fase.lancar(45, 1)
    fase.lancar(64, 2)
    fase.lancar(23, 3)

    animar(root,fase)

    # root.wait_window(popup_angulo)
