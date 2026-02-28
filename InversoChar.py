# lê N
linha = input().strip()
while linha == "":
    linha = input().strip()

N = int(linha)

# lê a linha com N caracteres separados por espaço
vetor = input().split()

# imprime do último para o primeiro
i = N - 1
while i >= 0:
    if i == 0:
        # último da saída: sem espaço depois
        print(vetor[i])
    else:
        # demais: seguido de espaço, sem quebra de linha ainda
        print(vetor[i], end=" ")
    i -= 1