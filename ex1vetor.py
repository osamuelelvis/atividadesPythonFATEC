def main():
    ls = [0]*50
    soma = 0
    contador = 0
    soma_impares = 0

    for i in range (5):
        ls[i] = int(input("Digite um valor entre 10 e 200: "))

        if (ls[i] >= 10 and ls[i] <= 200):
            soma = soma + ls[i]
            contador += 1

        if (ls[i] % 2 == 1):
            soma_impares = soma_impares + ls[i]

    if (contador > 0):
        media = soma / contador
        print(f"Média: {media}")

    if (soma_impares > 0):
        print(f"Soma ímpares: {soma_impares}")

if __name__ == '__main__':
    main()