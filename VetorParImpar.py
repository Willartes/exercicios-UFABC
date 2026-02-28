entrada = input().strip()
N = int(entrada)

while N != 0:
    # Lê a linha com N inteiros
    linha = input().split()

    # Converte para int e já transforma par -> 0, ímpar -> 1
    i = 0
    while i < N:
        valor = int(linha[i])
        if valor % 2 == 0:
            linha[i] = '0'
        else:
            linha[i] = '1'
        i += 1

    # Imprime os N valores separados por espaço e depois quebra a linha
    i = 0
    while i < N:
        if i == N - 1:
            print(linha[i])
        else:
            print(linha[i], end=' ')
        i += 1

    # Lê o próximo N
    entrada = input().strip()
    N = int(entrada)
