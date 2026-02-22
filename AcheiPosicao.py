N = int(input())

linha = input().split()
V = []
for i in range(N):
    V.append(int(linha[i]))

M = int(input())

# Para cada busca, procurar o número em V
for _ in range(M):
    x = int(input())

    posicao = -1  # valor padrão (não encontrado)

    # Procura a primeira ocorrência de x em V
    for i in range(N):
        if V[i] == x:
            posicao = i
            break  # já achou a primeira, pode parar

    print(posicao)
