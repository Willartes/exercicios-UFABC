n = int(input())
m = int(input())

matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for j in range(m):
    for i in range(n):
        print(matriz[i][j], end="")
        if i < n - 1:
            print(" ", end="")
    print()
