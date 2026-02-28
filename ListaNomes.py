linha = input().strip()
while linha == "":
    linha = input().strip()

N = int(linha)

nomes = [None] * N

i = 0
while i < N:
    nome = input().rstrip("\n")
    nomes[i] = nome
    i += 1

i = N - 1
while i >= 0:
    print(nomes[i])
    i -= 1