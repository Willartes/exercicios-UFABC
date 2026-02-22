N, M = map(int, input().split())
matriz = []
for _ in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)
menor_valor = float('inf')
for j in range(M):
    soma_avenida = 0
    for i in range(N):
        soma_avenida += matriz[i][j]
    if soma_avenida < menor_valor:
        menor_valor = soma_avenida
print(menor_valor)
