import threading
import time

def tarefa(id):
    time.sleep(0.5)
    print("Thread #", id)

for i in range(5):
    t = threading.Thread(target=tarefa, args=(i,))
    t.start()