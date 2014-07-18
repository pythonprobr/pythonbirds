#coding: utf-8
import time

from tkinter import *
from tkinter import ttk
from fase import Fase
from atores import PassaroVermelho, PassaroAmarelo, Porco, Obstaculo


def get_angulo(event):
    global angulo_input, popup_angulo
    print(angulo_input.get())
    popup_angulo.destroy()


root = Tk()
root.title("Python Birds")
root.geometry("800x600")
root.resizable(0, 0)

stage = Canvas(root, width=800, height=600)
bg_image = PhotoImage(file="images/background.gif")
stage.create_image((0, 0), image=bg_image, anchor=NW)
stage.pack()

passaro_vermelho_img = PhotoImage(file="images/passaro_vermelho.gif")
passaro_vermelho = stage.create_image((40, 482), image=passaro_vermelho_img, anchor=NW)

passaro_amarelo_img = PhotoImage(file="images/passaro_amarelo.gif")
passaro_amarelo = stage.create_image((30, 482), image=passaro_amarelo_img, anchor=NW)

passaro_amarelo2 = stage.create_image((20, 482), image=passaro_amarelo_img, anchor=NW)

porco_img = PhotoImage(file="images/porco.gif")
porco = stage.create_image((700, 482), image=porco_img, anchor=NW)

porco2 = stage.create_image((480, 482), image=porco_img, anchor=NW)

obstaculo_img = PhotoImage(file="images/obstaculo.gif")
obstaculo = stage.create_image((300, 300), image=obstaculo_img, anchor=NW)


# popup_angulo = Toplevel(root)
# Label(popup_angulo, text="Digite o angulo de lançamento: ").pack()
# angulo_input = Entry(popup_angulo)
# angulo_input.pack(padx=6)
# b = Button(popup_angulo, text="OK", command=get_angulo)
# b.pack(pady=5)


def mover(obj, x, y):
    stage.move(obj, x, y)
    stage.update()

tempo = 0
passo = 0.1
delta_t = 0.1

passaros = [passaro_vermelho, passaro_amarelo]
fase = None

ultima_posicao = {}

def mover(canvas_id, posicao_atual, proxima_posicao):
    if proxima_posicao.y == 0: 
        return

    x = posicao_atual.x - proxima_posicao.x
    y = posicao_atual.y - proxima_posicao.y
    stage.move(canvas_id, -x * 30, y * 30)

def animar():
    global tempo, delta_t, fase       
    tempo += delta_t
    time.sleep(passo)
    pontos_cartesianos = fase.calcular_pontos(tempo)
    for ponto in pontos_cartesianos:
        canvas_id = ponto.canvas
        ultima_posicao[canvas_id] = ultima_posicao.get(canvas_id, ponto)
        mover(canvas_id, ultima_posicao[canvas_id], ponto)
        #verificar aqui colisão


        ultima_posicao[canvas_id] = ponto

    root.after(1, animar)


fase = Fase()
passaros = [PassaroVermelho(3, 3, passaro_vermelho), PassaroAmarelo(3, 3, passaro_amarelo), PassaroAmarelo(3, 3, passaro_amarelo2)]
porcos = [Porco(78, 1, porco), Porco(78, 1, porco2)]
obstaculos = [Obstaculo(31, 10, obstaculo)]

fase.adicionar_passaro(*passaros)
fase.adicionar_porco(*porcos)
fase.adicionar_obstaculo(*obstaculos)


fase.lancar(45, 1)
fase.lancar(64, 2)
fase.lancar(23, 3)

root.after(1, animar)
root.mainloop()

# root.wait_window(popup_angulo)
