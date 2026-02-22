linha = input().split()
N = int(linha[0])
C = int(linha[1])
M = int(linha[2])

linha_carimbadas = input().split()
carimbadas = []
for i in range(C):
    carimbadas.append(int(linha_carimbadas[i]))


linha_compradas = input().split()

comprada = [False] * (N + 1)

for i in range(M):
    fig = int(linha_compradas[i])
    if 1 <= fig <= N:
        comprada[fig] = True

faltam = 0
for i in range(C):
    fig = carimbadas[i]
    if not comprada[fig]:
        faltam += 1

print(faltam)
