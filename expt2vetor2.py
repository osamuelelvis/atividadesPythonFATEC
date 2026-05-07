import platform
import subprocess

def os():
    return platform.system()

def main():
    if os() == 'Windows':
        print("Esse PC é um Windows")
    else:
        print("Esse PC é um Linux")

    while True:
        print("1 - Listar processos")
        print("2 - Matar por PID")
        print("3 - Matar por nome")
        print("9 - Encerrar")
        opcao = int(input("Escolha: "))

        if opcao == 1:
            print("Listando processos...")
            so = os()
            if so == 'Windows':
                comando = 'TASKLIST /FO TABLE'
            else:
                comando = 'ps -ef'
            
            executar(comando)

        elif opcao == 2:
            pid = input("Digite o PID do processo a ser morto: ")
            so = os()
            if so == 'Windows':
                comando = f'TASKKILL /PID {pid}'
            else:
                comando = f'kill -9 {pid}'

            executar(comando)

        elif opcao == 3:
            nome = input("Digite o nome do processo a ser morto: ")
            so = os()
            if so == 'Windows':
                comando = f'TASKKILL /IM {nome}'
            else:
                comando = f'pkill -f {nome}'

            executar(comando)

        elif opcao == 9:
            print("Encerrando...")
            break

def executar(comando):
    resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)
    print(resultado.stdout)

if __name__ == '__main__':
    main()