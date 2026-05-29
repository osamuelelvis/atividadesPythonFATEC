import threading
import time
import random

pista_norte = threading.Semaphore(1)
pista_sul = threading.Semaphore(1)
area_decolagem = threading.Semaphore(2)

semaforo1 = None
semaforo2 = None

def aviao(id):
    print(f"\nAvião #{id} aguardando área de decolagem")

    with area_decolagem:

        print(f"Avião #{id} entrou na área")

        pista_escolhida = random.choice(["norte", "sul"])

        if pista_escolhida == "norte":
            with pista_norte:

                print(f"Avião #{id} usando pista NORTE")

                manobra(id)
                taxiamento(id)
                decolagem(id)
                afastamento(id)

        else:
            with pista_sul:

                print(f"Avião #{id} usando pista SUL")

                manobra(id)
                taxiamento(id)
                decolagem(id)
                afastamento(id)
            
    print(f"Avião #{id} saiu da área")
        
def manobra(id):
    print(f"Avião #{id} está manobrando")
    tempo = random.uniform(0.3, 0.7)
    time.sleep(tempo)

def taxiamento(id):
    print(f"Avião #{id} está taxiando")
    tempo = random.uniform(0.5, 1.0)
    time.sleep(tempo)
    
def decolagem(id):
    print(f"Avião #{id} decolando")
    tempo = random.uniform(0.6, 0.8)
    time.sleep(tempo)

def afastamento(id):
    print(f"Avião #{id} afastando da área")
    tempo = random.uniform(0.3, 0.8)
    time.sleep(tempo)

def main():

    threads = []

    for i in range(12):
        t = threading.Thread(target=aviao, args=(i+1,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()