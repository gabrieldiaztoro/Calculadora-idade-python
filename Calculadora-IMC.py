from tkinter import*
from tkinter import ttk
from turtle import width

janela =Tk()
janela.title ("Calculadora IMC - CSV19")
janela.geometry ('310x400')

# cores
cor1 = "#3b3b3b"

#-------criando frames----
frame_topo = Frame(janela, width=310, height=150, pady=0, padx=0, relief=FLAT, bg=cor1) 
#- parte de cima da calculadora relief = estilo   'flat' ou FLAT, bg = background
frame_topo.grid(row=0, column=0)







janela.mainloop()