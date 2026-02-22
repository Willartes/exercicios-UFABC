op = input().strip()


N = int(input())

soma = 0.0
qtd = 0


for i in range(N):
    linha = input().split()

    for j in range(N):
        valor = int(linha[j])

        if j > i:
            soma += valor
            qtd += 1


if op == 'S':
    resultado = soma
else:
    resultado = soma / qtd

print(f"{resultado:.1f}")
