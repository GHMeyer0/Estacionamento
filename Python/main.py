import threading
import vagas
import threading as t
import time
import random

estacionamento = vagas.Vaga(10)

#cancelas = {
#    cancela1: t.Thread(target=thread_function, args=(1,)),
#        
#}

class Cancela(t.Thread):
    def carroEntrar(self):
        estacionamento.ocupaVaga()
    
    def carroSair(self):
        estacionamento.liberaVaga()

    def run(self):
        while True:
            IO = random.randint(0, 1)
            if IO == 1:
                self.carroEntrar()
            if IO == 0:
                self.carroSair()
        return

for i in range(10):
	cancela = Cancela()
	cancela.start()
