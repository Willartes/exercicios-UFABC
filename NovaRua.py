N, M = map(int, input().split())
matriz = []
for _ in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)
menor_valor = float('inf')
for i in range(N):
    soma_rua = 0
    for j in range(M):
        soma_rua += matriz[i][j]
    if soma_rua < menor_valor:
        menor_valor = soma_rua
print(menor_valor)
