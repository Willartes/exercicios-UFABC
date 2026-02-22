soma = 0
while True:
    try:
        N = eval(input())
        soma += N
    except EOFError:
        break

print(soma)
