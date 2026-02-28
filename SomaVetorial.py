N = int(input())

while N != 0:
    linha_v = input().split()
    
    linha_u = input().split()

    i = 0
    while i < N:
        v = float(linha_v[i])
        u = float(linha_u[i])
        w = v + u
        # imprime com duas casas decimais, controlando espaço
        if i == N - 1:
            print(f"{w:.2f}")
        else:
            print(f"{w:.2f}", end=' ')
        i += 1

    N = int(input())

