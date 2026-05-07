def main():
    vetor = [0]*30
    media = 0
    soma = 0
    contador = 0
    qtd_acima = 0
    qtd_abaixo = 0

    for i in range (30):
        vetor[i] = float(input("Digite uma nota entre 0 e 10: "))
        soma = soma + vetor[i]

    media = soma / 5

    for i in range (30):
        if (vetor[i] < media):
            qtd_abaixo += 1
        elif (vetor[i] > media):
            qtd_acima += 1

    print(f"Média: {media}")
    print(f"Quantidade de notas acima da média: {qtd_acima}")
    print(f"Quantidade de notas abaixo da média: {qtd_abaixo}")

if __name__ == '__main__':
    main()