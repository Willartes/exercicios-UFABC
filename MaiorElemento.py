# Leitura repetida de casos até N == 0
while True:
    linha = input().strip()
    if linha == "":
        continue  # ignora linhas vazias (se existirem)
    N = int(linha)

    if N == 0:
        break  # condição de parada

    # lê a linha com os N inteiros
    elementos = list(map(int, input().split()))

    # inicializa maior e índice do maior
    maior = elementos[0]
    indice_maior = 0  # índice começa em 0 (como no exemplo)

    # percorre o vetor para achar o maior e seu primeiro índice
    i = 1
    while i < N:
        if elementos[i] > maior:
            maior = elementos[i]
            indice_maior = i
        i += 1

    # imprime índice da primeira ocorrência do maior e o próprio maior
    print(indice_maior, maior)