linha = input().strip()
while linha == "":
    linha = input().strip()

N = int(linha)

v = list(map(int, input().split()))

maior = v[0]
menor = v[0]
i_maior = 0
i_menor = 0

i = 1
while i < N:
    if v[i] > maior:
        maior = v[i]
        i_maior = i
    if v[i] < menor:
        menor = v[i]
        i_menor = i
    i += 1

temp = v[i_maior]
v[i_maior] = v[i_menor]
v[i_menor] = temp

i = 0
while i < N:
    if i == N - 1:
        print(v[i])
    else:
        print(v[i], end=" ")
    i += 1