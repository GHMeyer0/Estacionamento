import threading
import vagas
import threading as t
import time
import random
import os


def clear(): return os.system('cls')  # on Windows System

estacionamento = vagas.Vaga(10)
class Cancela(t.Thread):
    def carroEntrar(self, quantidade_de_carros):
        for target_list in range(quantidade_de_carros):
            estacionamento.ocupaVaga()
        
    def carroSair(self, quantidade_de_carros):
        for target_list in range(quantidade_de_carros):
            estacionamento.liberaVaga()
        

    def run(self):
        while True:
            IO = random.randint(0, 1)
            if IO == 1:
                self.carroEntrar(random.randint(1,5))
            if IO == 0:
                self.carroSair(random.randint(1,5))
        return

for i in range(10):
	cancela = Cancela()
	cancela.start()
