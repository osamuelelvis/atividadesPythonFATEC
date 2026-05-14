import threading
import random
import time

DISTANCIA_MAXIMA = 50
SALTO_MAXIMO = 5

def corrida_sapo(id):
    distancia = 0

    while distancia < DISTANCIA_MAXIMA:
        salto = random.randint(1, SALTO_MAXIMO)

        distancia += salto

        if distancia > DISTANCIA_MAXIMA:
            distancia = DISTANCIA_MAXIMA

        print(f"Sapo {id} pulou {salto}cm  e chegoou em {distancia}cm")

        time.sleep(0.2)

    print(f"Sapo {id} chegou na linha de chegada!")

def main():
    threads = []
    for i in range (1, 6):
        t = threading.Thread(target=corrida_sapo, args=(i,))

        threads.append(t)

        t.start()

    for t in threads:
        t.join()

    print("Corrida finalizada!")

if __name__ == '__main__':
    main()