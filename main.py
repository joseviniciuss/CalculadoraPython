from tkinter import *
from tkinter import ttk 

preto = "#000000"
cinzaEscuro = "#1C1C1C"
cinzaMedio = "#363636"
cinzaClaro = "#808080"
brancoCinza = "#DCDCDC"

janela = Tk()
janela.title("Calculadora")
janela.geometry("318x470")
janela.config(bg = cinzaEscuro)


#DIVISÃO DE TELA

frameDisplay = Frame(janela, width = 318, height = 90, background = cinzaEscuro)
frameDisplay.grid(row = 0, column = 0)

frameTeclas = Frame(janela, width = 318, height = 380, background= cinzaEscuro)
frameTeclas.grid(row = 1, column = 0)


#LABEL

valorTexto = StringVar()


numerosLabel = Label(frameDisplay, textvariable = valorTexto, width = 16, height = 3, padx = 7, relief = FLAT, anchor = "e", justify = RIGHT, font = ('Ivy 24 bold'), bg = cinzaEscuro, fg = cinzaClaro)
numerosLabel.place(x = 0, y = 0)


#FUNÇÕES

todosValores = ""

def entradaDeValores(valorPressionado = ''):


    global todosValores

    todosValores = todosValores + str(valorPressionado)

    valorTexto.set(todosValores)

def calcular():

    global todosValores

    resultado = eval(todosValores)
    
    valorTexto.set(resultado)

def limparValores():

    global todosValores

    todosValores = ""
    valorTexto.set("")


#PRIMEIRA LINHA DE BOTÕES

botaoLimpar = Button(frameTeclas, command = limparValores, text = "C", width = 20, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botaoLimpar.place(x=7, y=5)

botaoPorcentagem = Button(frameTeclas, command = lambda: entradaDeValores('%'), text = "%", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botaoPorcentagem.place(x=162, y=5)

botaoDividir = Button(frameTeclas, command = lambda: entradaDeValores('/'), text = "/", width = 9, height = 4, bg= cinzaClaro , relief = RAISED, overrelief = RIDGE)
botaoDividir.place(x=240, y=5)

#SEGUNDA LINHA DE BOTÕES

botao7 = Button(frameTeclas, command = lambda: entradaDeValores('7'), text = "7", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao7.place(x= 7, y= 80)

botao8= Button(frameTeclas, command = lambda: entradaDeValores('8'), text = "8", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao8.place(x= 84, y= 80)

botao9 = Button(frameTeclas, command = lambda: entradaDeValores('9'), text = "9", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao9.place(x= 162, y= 80)

botaoMultiplicar = Button(frameTeclas, command = lambda: entradaDeValores('*'), text = "*", width = 9, height = 4, bg= cinzaClaro , relief = RAISED, overrelief = RIDGE)
botaoMultiplicar.place(x=240, y=80)

#TERCEIRA LINHA DE BOTÕES

botao4 = Button(frameTeclas, command = lambda: entradaDeValores('4'), text = "4", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao4.place(x= 7, y= 155)

botao5 = Button(frameTeclas, command = lambda: entradaDeValores('5'), text = "5", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao5.place(x= 84, y= 155)

botao6 = Button(frameTeclas, command = lambda: entradaDeValores('6'), text = "6", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao6.place(x= 162, y= 155)

botaoMenos = Button(frameTeclas, command = lambda: entradaDeValores('-'), text = "-", width = 9, height = 4, bg= cinzaClaro , relief = RAISED, overrelief = RIDGE)
botaoMenos.place(x=240, y=155)

#QUARTA LINHA DE BOTÕES

botao1 = Button(frameTeclas, command = lambda: entradaDeValores('1'), text = "1", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao1.place(x= 7, y= 230)

botao2 = Button(frameTeclas, command = lambda: entradaDeValores('2'), text = "2", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao2.place(x= 84, y= 230)

botao3 = Button(frameTeclas, command = lambda: entradaDeValores('3'), text = "3", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botao3.place(x= 162, y= 230)

botaoMais = Button(frameTeclas, command = lambda: entradaDeValores('+'), text = "+", width = 9, height = 4, bg= cinzaClaro , relief = RAISED, overrelief = RIDGE)
botaoMais.place(x=240, y=230)

#QUINTA LINHA DE BOTÕES

botaoZero = Button(frameTeclas, command = lambda: entradaDeValores('0'), text = "0", width = 20, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botaoZero.place(x=7, y=305)

botaoPonto = Button(frameTeclas, command = lambda: entradaDeValores('.'), text = ".", width = 9, height = 4, bg= cinzaMedio, fg = brancoCinza , relief = RAISED, overrelief = RIDGE)
botaoPonto.place(x= 162, y= 305)

botaoIgual = Button(frameTeclas, command = calcular, text = "=", width = 9, height = 4, bg= cinzaClaro , relief = RAISED, overrelief = RIDGE)
botaoIgual.place(x=240, y=305)



janela.mainloop()