import threading
import platform
import subprocess
import re

def ping_servidor(nome, servidor):

    sistema = platform.system()

    if sistema == 'Windows':
        comando = ["ping", "-4", "-n", "10", servidor]

    elif sistema == 'Linux':
        comando = ["ping", "-4", "-c", "10", servidor]

    else:
        print("Sistema operacional não suportado.")
        return
    
    processo = subprocess.Popen(
        comando,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    tempos = []

    for linha in processo.stdout:

        linha = linha.lower()

        if "tempo=" in linha or "time=" in linha:

            resultado = re.search(r'(\d+)\s*ms', linha)

            if resultado:

                tempo = int(resultado.group(1))

                tempos.append(tempo)

                print(f"{nome} -> Tempo: {tempo} ms")

    if len(tempos) > 0:

        media = sum(tempos) / len(tempos)

        print(f"{nome} -> Tempo médio: {media:.2f} ms")

def main():

    threads = []

    servidores = [
        ("UOL", "www.uol.com.br"),
        ("Terra", "www.terra.com.br"),
        ("Google", "www.google.com.br")
    ]

    for nome, servidor in servidores:

        t = threading.Thread(
            target=ping_servidor,
            args=(nome, servidor)
        )
        
    threads.append(t)
    
    t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()