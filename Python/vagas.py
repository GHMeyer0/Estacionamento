import threading

class Vaga:
    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.vagas = []
        for vaga in range(self):
            vagas.append({
                'numero': vaga + 1,
                'disponivel': threading.Semaphore(1)
            })
        
    def preencheVaga(self):
        numero_da_vaga = self.buscaVagaDisponivel()
        if numero_da_vaga != False:
            self.vagas[numero_da_vaga - 1]['disponivel'].acquire()
        else:
            print("Vagas Esgotadas")
        

    def liberaVaga():

        __self__.vagas[numero_vaga - 1]['disponivel'].release()

    def buscaVagaDisponivel(self):
        for vaga in self.vagas:
            if vaga['disponivel']._value:
                return vaga['numero']
        return False
