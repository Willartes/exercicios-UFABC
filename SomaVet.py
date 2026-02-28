N = int(input())

valores = input().split()

soma = 0
i = 0
while i < N:
    soma = soma + int(valores[i])
    i = i + 1

print(soma)
