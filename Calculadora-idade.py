from tkinter import *
from tkinter import ttk

# importando tkcalendar
from tkcalendar import Calendar, DateEntry

# importando dateutil
from dateutil.relativedelta import relativedelta

# importando datetime
from datetime import date

# importando pillow, para adicionar imagens
from PIL import Image, ImageTk

janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry('310x400')

# cores
cor1 = "#3B3B3B"  # --cinza
cor2 = "#333333"  # --cinza escuro
cor3 = "#FFFFFF"  # --branca
cor4 = "#FF8C00"  # --laranja

# IMPORTANDO IMAGEM
#logo = Image.open('aqruivos/idade.png')
#logo = logo.resize((50,50), Image.ANTIALIAS)
#logo = ImageTk.PhotoImage(logo)

# -------criando frames----
frame_cima = Frame(janela, width=310, height=140,
                   pady=0, padx=0, relief=FLAT, bg=cor2)
# - parte de cima da calculadora relief = estilo   'flat' ou FLAT, bg = background
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300,
                    pady=0, padx=0, relief=FLAT, bg=cor1)
# fg = cor letra
# - parte de cima da calculadora relief = estilo   'flat' ou FLAT, bg = background
frame_baixo.grid(row=1, column=0)


# ----criando label para frame (Top)

l_calculadora = Label(frame_cima, text="CALCULADORA", width=18, height=1, padx=3,
                      relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0,
                relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor2, fg=cor4)
l_idade.place(x=-0, y=70)


# calculando idade //// esta parte foi adicionado por ultimo....


def calcular():
    inicial = cal_1.get()
    terminio = cal_2.get()

    # separando os valores
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]

    # convertendo os valores em datetime
    data_inicial = date(ano_1, mes_1, dia_1)

    # separando os valores
    mes_2, dia_2, ano_2 = [int(f) for f in terminio.split('/')]

    # convertendo os valores em datetime
    data_nascimento = date(ano_2, mes_2, dia_2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias

# ----criando label para frame (baixo)


l_data_inicial = Label(frame_baixo, text="Data de hoje", padx=0, pady=0, relief='flat',
                       anchor=NW, font=('Ivi 11 bold'), bg=cor1, fg=cor3)  # anchor=NM = north west
l_data_inicial.place(x=20, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3,
                  borderwidth=2, date_pattern='mm/dd/y', y=2022)
cal_1.place(x=180, y=30)

l_data_nascimento = Label(frame_baixo, text="Data de nascimento", width=25, height=1,
                          padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor1, fg=cor3)
l_data_nascimento.place(x=20, y=70)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3,
                  borderwidth=2, date_pattern='mm/dd/y', y=2022)
cal_2.place(x=180, y=70)

# resultado
l_app_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0,
                   relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor1, fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="anos",   height=1, padx=0,
                        pady=0, relief='flat', anchor=NW, font=('Ivi 11 bold'), bg=cor1, fg=cor3)
l_app_anos_nome.place(x=60, y=175)


l_app_meses = Label(frame_baixo, text="--", width=25, height=1, padx=0,
                    pady=0, relief='flat', anchor=NW, font=('Ivi 25 bold'), bg=cor1, fg=cor3)
l_app_meses.place(x=140, y=130)
l_app_meses_nome = Label(frame_baixo, text="meses", width=25, height=1, padx=0,
                         pady=0, relief='flat', anchor=NW, font=('Ivi 13 bold'), bg=cor1, fg=cor3)
l_app_meses_nome.place(x=140, y=175)

l_app_dias = Label(frame_baixo, text="--", width=25, height=1, padx=0,
                   pady=0, relief='flat', anchor=NW, font=('Ivi 25 bold'), bg=cor1, fg=cor3)
l_app_dias.place(x=220, y=130)
l_app_dias_nome = Label(frame_baixo, text="dias", width=25, height=1, padx=0,
                        pady=0, relief='flat', anchor=NW, font=('Ivi 13 bold'), bg=cor1, fg=cor3)
l_app_dias_nome.place(x=220, y=175)

# botao calcular

b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1,
                    relief='raised', overrelief='ridge', font=('Ivi 10 bold'), bg=cor1, fg=cor3)
b_calcular.place(x=70, y=225)

janela.mainloop()
