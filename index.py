import pandas as pd
import re
import pyautogui as pag
import time
import xlrd
import keyboard


from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from tkinter.messagebox import *

# df = pd.read_excel('C:/Users/forda/Desktop/arquivo.xlsx')

def startProject(FILE):
    df_ = pd.read_excel(FILE)
    df_ = df_.dropna(axis=1)

    data = df_['Order Refs']

    df_ = pd.DataFrame(data)

    # Usando split para separar os valores por vírgula e explodir a coluna
    df_['Order'] = df_['Order Refs'].str.split(',')
    df_ = df_.explode('Order')

    dados = df_['Order']

    # Expressão regular para remover a partir do '_'
    padrao = re.compile(r"_.*")
    resultados = []

    # Processamento dos dados
    for dado in dados:
        resultado = re.sub(padrao, "", dado)
        resultados.append(resultado)



    quantidade = len(resultados)
    pag.moveTo(1430, 350)
    pag.click()

    addDelay = float(entrada.get().replace(",", ".")
)
    print(addDelay)

    for i in resultados:
        pag.write(i)
        pag.moveTo(1430, 350)
        time.sleep(addDelay)
        pag.click()
        print(i)

    # for x in range(quantidade):
    #     pag.moveTo(1430, 350)
    #     # localizacaoBotao = pag.locateOnScreen('botaoAdc.png')
    #     # pag.moveTo(localizacaoBotao[0] + 5 ,localizacaoBotao[1]+ 10, confidence= 0.45)
        
    #     time.sleep(0.005)
    #     print(x)
    #     pag.click()


    # pag.locateOnScreen('invoice.png')
    # pag.moveTo(774, 377)
    # localizacaoBotao = pag.locateOnScreen('invoice.png', confidence= 0.45)
    # pag.moveTo(localizacaoBotao[0] + 50 ,localizacaoBotao[1]+ 22)
    # pag.click()


    #pegar valor da lista
    # for i in resultados:
    #     pag.write(i)
    #     # pag.press('down')
    #     print(i)

def process(FILE):
    print(FILE)
    if not FILE:
        return False
    else:
        startProject(FILE)


# interface




janela = Tk()
janela.title('Project Irio')
janela.geometry("200x200")
janela.resizable(0, 0)


FILE = '-'

def botao_enviararquivo():
    global FILE
    file = askopenfile(initialdir="C:/", mode='r')
    FILE = file.name
    texto_orientacao4 = Label(janela, text='Selecionado!', font='Courier 11')
    texto_orientacao4.place(x=40, y=140)


texto_orientacao = Label(janela, text='Bem vindo!')
texto_orientacao.pack()
texto_orientacao.configure(font=("Courier", 16, "bold"))

btn_arquivo = Button(janela, text='Selecione seu arquivo', command=lambda: botao_enviararquivo())
btn_arquivo.pack()

label = Label (janela, text = "Delay(segundos):")
label.pack()



entrada = Entry(janela,width=10)
entrada.pack()




processar_arq = Button(janela, text='Processar Arquivo', command=lambda: [entrada.get(), process(FILE), msg()])
processar_arq.pack()



print(entrada)


def msg():
    msg1= "Processo finalizado!"
    showinfo("Alerta!", msg1)

janela.mainloop()