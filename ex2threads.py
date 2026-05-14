import threading
import random
import time

def calcular_soma(id, valores):
    soma = 0
    for valor in valores:
        soma += valor
        time.sleep(0.2)

    print(f"Linha {id} -> Soma = {soma}")

def main():
    threads = []
    for id in range(3):
        valores = []

        for i in range(5):
            valores.append(random.randint(1, 100))

        print (f"Linha {id}: {valores}")

        t = threading.Thread(target=calcular_soma, args=(id, valores))

        threads.append(t)

        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()