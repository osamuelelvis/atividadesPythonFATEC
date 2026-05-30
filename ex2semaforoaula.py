import threading 
import time 
import random

sem_tocha = threading.Semaphore(1)
dono_tocha = None

sem_pedra = threading.Semaphore(1)
dono_pedra = None

sem_porta = threading.Semaphore(1)
portas = [1, 2, 3, 4]
porta_saida = random.randint(1, 4)

def cavaleiro(id):
    global dono_tocha, dono_pedra
    possui_tocha = False

    tentou_tocha = False
    tentou_pedra = False

    posicao = 0

    velocidade = random.randint(2,4)

    while posicao < 2000:
        posicao += velocidade

        if posicao >= 500 and not tentou_tocha:
            tentou_tocha = True

            with sem_tocha:
                if dono_tocha is None:
                    dono_tocha = id
                    possui_tocha = True
                    velocidade += 2
                    print(f"Cavaleiro #{id} pegou a tocha")

        if posicao >= 1500 and not tentou_pedra and not possui_tocha:
            tentou_pedra = True
            
            if not possui_tocha:
                with sem_pedra:
                    if dono_pedra is None:
                        dono_pedra = id
                        velocidade += 2
                        print(f"Cavaleiro #{id} pegou a pedra")

        print(f"Cavaleiro #{id} -> {posicao}m")

        time.sleep(0.05)

    print(f"Cavaleiro #{id} chegou ao final")

    with sem_porta:
        porta = random.choice(portas)
        portas.remove(porta)
        print(f"Cavaleiro #{id} escolheu a porta {porta}")

        if porta == porta_saida:
            print(f"Cavaleiro #{id} venceu!")
        else:
            print(f"Cavaleiro #{id} foi devorado!")

def main():
    threads = []

    for i in range(4):
        t = threading.Thread(target=cavaleiro, args=(i+1,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()