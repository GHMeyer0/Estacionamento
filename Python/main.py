from tkinter import *
import threading
import vagas
import threading as t
import time
import random
import os

def clear(): return os.system('cls')  # on Windows System

estacionamento = vagas.Vaga(10)
fila_pra_entrar = 1000
fila_pra_sair = 0

class Cancela(t.Thread):
    def carroEntrar(self, quantidade_de_carros):
        for target_list in range(quantidade_de_carros):
            estacionamento.ocupaVaga()

        
    def carroSair(self, quantidade_de_carros):
        for target_list in range(quantidade_de_carros):
            estacionamento.liberaVaga()


    def run(self):
        global fila_pra_entrar
        global fila_pra_sair
        while fila_pra_entrar > 0:
            IO = random.randint(0,1)
            if IO == 1:
                self.carroEntrar(1)
                fila_pra_entrar -= 1
                fila_pra_sair += 1
            if IO == 0:
                self.carroSair(1)
                fila_pra_sair -= 1
        return
    

class Application:
    fontPadrao = ("Verdana", "10", "italic")
    fontPadraoNegrito = ("Verdana", "10", "italic", "bold")
    def __init__(self, master=None):
        def callback():
            print(self.quantCarrosEntrar.get())
            cancela = Cancela()
            for target_list in range(3):
                cancela = Cancela()
                cancela.start()
            
        self.mainContainer = Frame(master)
        self.mainContainer.pack()
        self.msg = Label(self.mainContainer, text="Estacionamento")
        self.msg["font"] = self.fontPadraoNegrito
        self.msg.pack ()

        self.quantCancelasMsg = Label(self.mainContainer, text="Quantidade de cancelas")
        self.quantCancelasMsg["font"] = self.fontPadrao
        self.quantCancelasMsg.pack()

        self.quantCancelas = Entry(self.mainContainer)
        self.quantCancelas["width"] = 10
        self.quantCancelas["font"] = self.fontPadrao
        self.quantCancelas.pack(side=TOP)

        self.sairMsg = Label(self.mainContainer, text="Quantidade de carros")
        self.sairMsg["font"] = self.fontPadrao
        self.sairMsg.pack()

        self.quantCarrosSair = Entry(self.mainContainer)
        self.quantCarrosSair["width"] = 10
        self.quantCarrosSair["font"] = self.fontPadrao
        self.quantCarrosSair.pack(side=TOP)

        self.sair = Button(self.mainContainer)
        self.sair["text"] = "Sair carro"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 10
        self.sair["command"] = Cancela.carroSair(self, 1)
        self.sair.pack ()

        self.entrarMsg = Label(self.mainContainer, text="Quantidade de carros")
        self.entrarMsg["font"] = self.fontPadrao
        self.entrarMsg.pack()

        self.quantCarrosEntrar = Entry(self.mainContainer)
        self.quantCarrosEntrar["width"] = 10
        self.quantCarrosEntrar["font"] = self.fontPadrao
        self.quantCarrosEntrar.pack(side=TOP)
        self.entrar = Button(self.mainContainer, command=callback)
        self.entrar["text"] = "Entrar carro"
        self.entrar["font"] = self.fontPadrao
        self.entrar["width"] = 10
        self.entrar.pack()

root = Tk()
Application(root)
root.mainloop()

