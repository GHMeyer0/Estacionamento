import threading
import time
vagas = []
cancelas = []

def criar_vagas(quantidade_de_vagas):
    for vaga in range(quantidade_de_vagas):
        vagas.append({
            'numero': vaga + 1,
            'disponivel': threading.Semaphore(1)
        })

def vaga_esta_disponivel(vaga):
    if vaga['disponivel']._value:
        return True
    return False

def busca_vaga_disponivel():
    for vaga in vagas:
        if vaga_esta_disponivel(vaga):
            return vaga['numero']
def busca_vaga_ocupada():
    for vaga in vagas:
        if not vaga_esta_disponivel(vaga):
            return vaga['numero']

def apertar_botao(IO):
    if IO == "i" or IO == "I":
        entra_carro()
    else:
        sai_carro()
    time.sleep(10)

def entra_carro():
    numero_vaga = busca_vaga_disponivel()
    print('Favor se Dirigir a vaga ', numero_vaga )
    vagas[numero_vaga - 1]['disponivel'].acquire()

def sai_carro():
        numero_vaga = busca_vaga_ocupada()
        vagas[numero_vaga - 1]['disponivel'].release()
        print('Vaga numero ', numero_vaga, 'Liberada')

criar_vagas(30)
while True:
    botap = input()
    for cancela in range(4):
        cancelas[cancela].append(threading.Thread(target=apertar_botao, args=botap))
        if not cancelas[cancela].isAlive:
            cancelas[cancela].start()
    
    treads = threading.enumerate()
    print("Threades")
    
    for cancela in range(4):
        cancelas[cancela].join()






