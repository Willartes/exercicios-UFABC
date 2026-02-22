n = int(input())

valores = list(map(int, input().split()))

quantidade_pares = 0

for numero in valores:
    if numero % 2 == 0:
        quantidade_pares += 1

for i in range(0, n, 2):
    print(valores[i], end=" ")

print(quantidade_pares)
