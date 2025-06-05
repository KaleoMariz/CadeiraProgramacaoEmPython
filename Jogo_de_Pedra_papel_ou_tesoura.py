import tkinter
from tkinter import *
from tkinter import ttk

# cores 

cor1 = "#020122" 
# fundo
cor2 = "#0A0929"
cor3 = "#141331"
cor4 = "#24233F"
cor5 = "#2E2D48" 
# letras
cor6 = "#FFFFFF" 

# janela

janela = Tk()
janela.title("Jokenpô")
janela.geometry("360x380+300+300")
janela.configure(bg=cor1)

#divisão da tela 

frame_cima  = Frame(janela, width = 360, height = 150, background = cor2, relief = "raised")
frame_cima.grid(row = 0, column = 0, sticky=NW)

frame_baixo  = Frame(janela, width = 360, height = 230, background = cor3, relief = "flat")
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#frame cima config

#player1
nome_1 = Label(frame_cima, text="Jogador", height= 1, anchor="center", font=('Arial 10 bold'), bg=cor2, fg=cor6)
nome_1.place(x=0, y=125)

nome_1_pontos = Label(frame_cima, text="0", height= 1, anchor="center", font=('Arial 30 bold'), bg=cor2, fg=cor6)
nome_1_pontos.place(x=70, y=60)

pontos1 = Label(frame_cima, text=":", height= 1, anchor="center", font=('Arial 30 bold'), bg=cor2, fg=cor6)
pontos1.place(x=170, y=60)
 
#player2
nome_2 = Label(frame_cima, text="Computador", height= 1, anchor="center", font=('Arial 10 bold'), bg=cor2, fg=cor6)
nome_2.place(x=275, y=125)

nome_2_pontos = Label(frame_cima, text="0", height= 1, anchor="center", font=('Arial 30 bold'), bg=cor2, fg=cor6)
nome_2_pontos.place(x=260, y=60)

pontos2 = Label(frame_cima, text=":", height= 1, anchor="center", font=('Arial 30 bold'), bg=cor2, fg=cor6)
pontos2.place(x=0, y=60)




janela.mainloop()