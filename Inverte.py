linha = input().strip()
while linha == "":
    linha = input().strip()

N = int(linha)

v = input().split()

i = 0
while i < N:
    if i == N - 1:
        print(v[i])
    else:
        print(v[i], end=" ")
    i += 1

i = N - 1
while i >= 0:
    if i == 0:
        print(v[i])
    else:
        print(v[i], end=" ")
    i -= 1