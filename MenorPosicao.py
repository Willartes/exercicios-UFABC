n = int(input())

valores = list(map(int, input().split()))

menor_valor = valores[0]
posicao = 0

for i in range(1, n):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
        posicao = i

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
