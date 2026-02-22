op = input().strip()


N = int(input())

soma = 0.0


for i in range(N):
    linha = input().split()


    valor = int(linha[i])
    soma += valor


if op == 'S':
    resultado = soma
else:  
    resultado = soma / N

print(f"{resultado:.1f}")
