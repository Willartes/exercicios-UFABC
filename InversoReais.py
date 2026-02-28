linha = input().strip()
while linha == "":
    linha = input().strip()

N = eval(linha)

valores = input().split()

i = N - 1
while i >= 0:
    if i == 0:
        print(valores[i])
    else:
        print(valores[i], end=" ")
    i -= 1