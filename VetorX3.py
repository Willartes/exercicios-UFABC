N = int(input())

valores = input().split()

# Constrói o vetor W com cada elemento de V multiplicado por 3
i = 0
while i < N:
    valor = int(valores[i])
    valor3 = valor * 3
    valores[i] = str(valor3)   # já guardo em string para impressão
    i += 1

# Imprime o vetor W na mesma linha, com espaço entre os elementos
i = 0
while i < N:
    if i == N - 1:
        print(valores[i])
    else:
        print(valores[i], end=' ')
    i += 1
