def main():
    vetor = [0]*5
    maior = 0
    menor = 0
    media = 0
    soma = 0
    contador = 0

    for i in range (5):
        vetor[i] = int(input("Digite um valor inteiro: "))
        soma = soma + vetor[i]
        contador += 1


    maior = vetor[0]
    menor = vetor[0]
    for i in range (5):
        if (vetor[i] > maior):
            maior = vetor[i]

        if (vetor[i] < menor):
            menor = vetor[i]


    if (contador > 0):
        media = soma / contador
        print(f"\nMédia: {media}")

    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")

if __name__ == '__main__':
    main()