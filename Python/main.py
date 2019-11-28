from tkinter import *
import threading
import vagas
import threading as t
import time
import random
import os

def clear(): return os.system('cls')  # on Windows System


lock = threading.Semaphore(1)
estacionamento = vagas.Vaga(10)
fila_pra_entrar = 1000
fila_pra_sair = 0

class Cancela(t.Thread): 
    global fila_pra_entrar
    global fila_pra_sair 

    def carroEntrar(self):
        global fila_pra_entrar
        global fila_pra_sair 

        lock.acquire()
        estacionamento.ocupaVaga() 
        fila_pra_entrar -= 1
        fila_pra_sair += 1
        lock.release()
    

    def carroSair(self):
        global fila_pra_entrar
        global fila_pra_sair 

        estacionamento.liberaVaga()
        fila_pra_sair -= 1
        lock.release()

    def run(self):
        while fila_pra_entrar > 0:
            InputOutput = random.randint(0,1)
            if InputOutput == 1:
                self.carroEntrar()
            if InputOutput == 0:
                self.carroSair()
            
        return



class Application:    
    fontPadrao = ("Verdana", "10", "italic")
    fontPadraoNegrito = ("Verdana", "10", "italic", "bold")

    def __init__(self, master=None):
        global fila_pra_sair
        fila_pra_sair_str = str(fila_pra_sair)

        def callback():
            print(self.quantCarrosEntrar.get())
            cancela = Cancela()
            for target_list in range(3):
                cancela = Cancela()
                cancela.start()

        self.mainContainer = Frame(master)
        self.mainContainer["width"] = 60
        self.mainContainer.pack()
        self.msg = Label(self.mainContainer, text="Estacionamento dos irmãos")
        self.msg["font"] = self.fontPadraoNegrito
        self.msg.pack ()

        self.quantCancelasMsg = Label(self.mainContainer, text="Quantidade de cancelas")
        self.quantCancelasMsg["font"] = self.fontPadrao
        self.quantCancelasMsg.pack()

        self.quantCancelas = Entry(self.mainContainer)
        self.quantCancelas["width"] = 40
        self.quantCancelas["font"] = self.fontPadrao
        self.quantCancelas.pack(side=TOP)

        self.quantCarrosMsg = Label(self.mainContainer, text="Quantidade de carros")
        self.quantCarrosMsg["font"] = self.fontPadrao
        self.quantCarrosMsg.pack()
        self.quantCarrosEntrar = Entry(self.mainContainer)
        self.quantCarrosEntrar["width"] = 40
        self.quantCarrosEntrar["font"] = self.fontPadrao
        self.quantCarrosEntrar.pack(side=TOP)

        self.entrar = Button(self.mainContainer, command=callback)
        self.entrar["text"] = "Entrar carros"
        self.entrar["font"] = self.fontPadrao
        self.entrar["width"] = 20
        self.entrar.pack()

        ##self.quantidadeDeVagasOcupadasMsg = Label(self.mainContainer, text=fila_pra_sair_str)
        ##self.quantidadeDeVagasOcupadasMsg["font"] = self.fontPadraoNegrito
        ##self.quantidadeDeVagasOcupadasMsg.pack()




root = Tk()
Application(root)
root.mainloop()
