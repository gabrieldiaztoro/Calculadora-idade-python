from cProfile import label
from tkinter import*
from tkinter import ttk
from turtle import width
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

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

#calculando idade //// esta parte foi adicionado por ultimo.... tinha terminado a linha 79 e foi incluido aqui nessa linha...

def calcular():
    hoje=cal_hoje.get()
    nascimento= cal_nascimento.get()

    anos =relativedelta(hoje, nascimento).years

#separando os valores
mes, dia, ano =[int(f) for f in hoje.split('/')]
data_hoje = date(ano, mes, dia) 


#----criando label para frame (Down)

l_data_inicial = Label(frame_down, text="Data de hoje", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor2 , fg=cor3) #anchor=NM = north west
l_data_inicial.place(x=20, y=30)

l_data_nascimento = Label(frame_down, text="Data de nascimento", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor2 , fg=cor3)
l_data_nascimento.place(x=20, y=70)

#calendario

cal_hoje = DateEntry(frame_down, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern= 'dd/mm/y', y=2022)
cal_hoje.place(x=180, y=30)

cal_nascimento = DateEntry(frame_down, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern= 'dd/mm/y', y=2022)
cal_nascimento.place(x=180, y=70)

#resultado
l_resultado_anos = Label(frame_down, text="27", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 25 bold'), bg=cor2 , fg=cor3)
l_resultado_anos.place(x=40, y=130)

l_resultado_anos2 = Label(frame_down, text="anos", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 13 bold'), bg=cor2 , fg=cor3)
l_resultado_anos2.place(x=40, y=170)


l_resultado_meses = Label(frame_down, text="8", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 25 bold'), bg=cor2 , fg=cor3)
l_resultado_meses.place(x=140, y=130)

l_resultado_meses2 = Label(frame_down, text="meses", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 13 bold'), bg=cor2 , fg=cor3)
l_resultado_meses2.place(x=130, y=170)



l_resultado_dias = Label(frame_down, text="90", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 25 bold'), bg=cor2 , fg=cor3)
l_resultado_dias.place(x=220, y=130)

l_resultado_dias2 = Label(frame_down, text="dias", width=25, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 13 bold'), bg=cor2 , fg=cor3)
l_resultado_dias2.place(x=220, y=170)


#botao calcular

b_calcular = Button(frame_down, command=calcular, text="Calcular",width=25, height=1, relief='raised', overrelief='ridge', font=('Ivi 10 bold'), bg=cor2 , fg=cor3)
b_calcular.place(x=55, y=210)






janela.mainloop()