# lê N
linha = input().strip()
while linha == "":
    linha = input().strip()

N = int(linha)

# lê a linha com N inteiros
valores = input().split()

# imprime do último para o primeiro
i = N - 1
while i >= 0:
    if i == 0:
        # último valor: sem espaço depois, mas com quebra de linha padrão do print
        print(valores[i])
    else:
        # demais valores: com espaço depois, sem quebra de linha ainda
        print(valores[i], end=" ")
    i -= 1