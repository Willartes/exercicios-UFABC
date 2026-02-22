n = int(input())


valores = list(map(int, input().split()))


pares = []


for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

for i in range(len(pares)):
    print(pares[i], end=' ')

print(len(pares))
