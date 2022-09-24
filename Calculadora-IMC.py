from cProfile import label
from tkinter import*
from tkinter import ttk
from turtle import width
from tkcalendar import Calendar, DateEntry

janela =Tk()
janela.title ("Calculadora IMC - CSV19")
janela.geometry ('310x400')

# cores
cor1 = "#333333" #--cinza escuro
cor2 = "#3B3B3B" #--cinza
cor3 = "#FFFFFF" #--branca
cor4 = "#FF8C00" #--laranja

#-------criando frames----
frame_top = Frame(janela, width=310, height=150, pady=0, padx=0, relief=FLAT, bg=cor1) 
#- parte de cima da calculadora relief = estilo   'flat' ou FLAT, bg = background
frame_top.grid(row=0, column=0)

frame_down = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cor2) 
#fg = cor letra
#- parte de cima da calculadora relief = estilo   'flat' ou FLAT, bg = background
frame_down.grid(row=1, column=0)


#----criando label para frame (Top)

l_calculadora = Label(frame_top, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg=cor1 , fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_top, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor1 , fg=cor4)
l_idade.place(x=-0, y=70)

#----criando label para frame (Down)

l_data_inicial = Label(frame_down, text="Data de hoje", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor2 , fg=cor3) #anchor=NM = north west
l_data_inicial.place(x=30, y=30)

l_data_nascimento = Label(frame_down, text="Data de nascimento", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor2 , fg=cor3)
l_data_nascimento.place(x=30, y=60)

#calendario

cal_hoje = DateEntry(frame_down, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_patter= mm/dd/y, y=2022)
cal_hoje.place(x=170, y=30)
janela.mainloop()