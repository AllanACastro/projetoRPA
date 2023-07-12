from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from tkinter import messagebox
from index import process, startProject

janela = Tk()
janela.title('Organizador - Estocão')
janela.geometry("200x200")
janela.resizable(0, 0)

FILE = '-'

def botao_enviararquivo():
    global FILE
    file = askopenfile(initialdir="C:/", mode='r', filetypes=[("Excel files", "*.xlsx")])
    FILE = file.name
    texto_orientacao4 = Label(janela, text='Selecionado!', font='Courier 11')
    texto_orientacao4.place(x=50, y=100)


texto_orientacao = Label(janela, text='Bem vindo!')
texto_orientacao.pack()
texto_orientacao.configure(font=("Courier", 16, "bold"))

btn_arquivo = Button(janela, text='Selecione seu arquivo', command=lambda: botao_enviararquivo())
btn_arquivo.pack()

processar_arq = Button(janela, text='Processar Arquivo', command=lambda: [process(FILE), msg()])
processar_arq.pack()

def msg():
    msg1= "Processo finalizado!"
    messagebox.showinfo("Alerta!", msg1)

janela.mainloop()