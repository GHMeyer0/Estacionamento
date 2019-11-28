import threading
import time

class Vaga:
    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.vagas = []
        for vaga in range(self.quantidade):
            self.vagas.append({
                'numero': vaga + 1,
                'vaga_disponivel': threading.Semaphore(1)
            })
            
    def ocupaVaga(self):
        numero_da_vaga = self.buscaVagaDisponivel()
        if numero_da_vaga != False:     
            self.vagas[numero_da_vaga - 1]['vaga_disponivel'].acquire()
            print("Vaga", numero_da_vaga, "Preenchida! \n ")
        else:
            print("Vagas Esgotadas")
        

    def liberaVaga(self):
        numero_da_vaga = self.buscaVagaOcupada()
        if numero_da_vaga != 0:
            self.vagas[numero_da_vaga - 1]['vaga_disponivel'].release()
            print("Vaga", numero_da_vaga, "Liberada! \n")
            time.sleep(2)
        else:
            "Todas as vagas estão vagas"


    def buscaVagaDisponivel(self):
        for vaga in self.vagas:
            if vaga['vaga_disponivel']._value == 1:
                return vaga['numero']
        return False
    
    def buscaVagaOcupada(self):
        for vaga in self.vagas:
            if vaga['vaga_disponivel']._value == 0:
                return vaga['numero']
            else:
                return 0
