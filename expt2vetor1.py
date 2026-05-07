import platform
import subprocess

def get_so():
    return platform.system()

def ping():
    so = get_so()
    if so == 'Windows':
        print("Esse PC é um Windows")
        comando = 'ping -4 -n 10 www.google.com.br' 
    else:
        print("Esse PC é um Linux")
        comando = 'ping -4 -c 10 www.google.com.br'

    resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)
    linhas = resultado.stdout.split('\n')
    ultima_linha = linhas[-2]

    if so == 'Windows':
        partes = ultima_linha.split(', ')
        media = partes[2].split(' = ')[1]
    else:
        ultima_linha = [l for l in linhas if 'avg' in l][0]
        media = ultima_linha.split('/')[4]

    print(f"Média de ping: {media}")

def main():
    ping()

if __name__ == '__main__':
    main()