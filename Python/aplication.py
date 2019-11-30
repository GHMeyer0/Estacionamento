from tkinter import *

class Application:    
    fontPadrao = ("Verdana", "10", "italic")
    fontPadraoNegrito = ("Verdana", "10", "italic", "bold")

    def setQuantVagasEntry(self):
        global quantidade_vagas
        quantidade_vagas = self.quantVagas.get()
        quantidade_vagas = int(quantidade_vagas)
    
    def setQuantCarrosEntry(self):
        global fila_pra_entrar
        fila_pra_entrar = self.quantCarrosEntrar.get()
        fila_pra_entrar = int(fila_pra_entrar)
    
    def setQuantCancelasEntry(self):
        global estacionamento
        self.setQuantVagasEntry()
        estacionamento = vagas.Vaga(quantidade_vagas)
        self.setQuantCarrosEntry()
        quantCancelas = self.quantCancelas.get()
        setQuantCancelas(quantCancelas)
        return quantCancelas

    def __init__(self, master=None):
        global fila_pra_sair
        global fila_pra_entrar

        self.mainContainer = Frame(master)
        self.mainContainer["width"] = 60
        self.mainContainer.pack()
        self.msg = Label(self.mainContainer, text="Estacionamento dos irmãos")
        self.msg["font"] = self.fontPadraoNegrito
        self.msg.pack ()

        self.quantVagasMsg = Label(self.mainContainer, text="Quantidade de vagas")
        self.quantVagasMsg["font"] = self.fontPadrao
        self.quantVagasMsg.pack()
        self.quantVagas = Entry(self.mainContainer)
        self.quantVagas["width"] = 40
        self.quantVagas["font"] = self.fontPadrao
        self.quantVagas.pack(side=TOP)

        self.quantCancelasMsg = Label(self.mainContainer, text="Quantidade de cancelas")
        self.quantCancelasMsg["font"] = self.fontPadrao
        self.quantCancelasMsg.pack()
        self.quantCancelas = Entry(self.mainContainer)
        self.quantCancelas["width"] = 40
        self.quantCancelas["font"] = self.fontPadrao
        self.quantCancelas.pack(side=TOP)

        self.quantCarrosMsg = Label(self.mainContainer, text="Quantidade de carros para entrar")
        self.quantCarrosMsg["font"] = self.fontPadrao
        self.quantCarrosMsg.pack()
        self.quantCarrosEntrar = Entry(self.mainContainer)
        self.quantCarrosEntrar["width"] = 40
        self.quantCarrosEntrar["font"] = self.fontPadrao
        self.quantCarrosEntrar.pack(side=TOP)

        self.entrar = Button(self.mainContainer)
        self.entrar["command"] = self.setQuantCancelasEntry
        self.entrar["text"] = "Entrar carros"
        self.entrar["font"] = self.fontPadrao
        self.entrar["width"] = 20
        self.entrar.pack()
