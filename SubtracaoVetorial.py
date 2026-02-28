n = int(input())

primeiro = True

while n != 0:
    v = input().split()
    u = input().split()

    if not primeiro:
        # nada especial, só segue imprimindo na mesma lógica
        pass
    else:
        primeiro = False

    resultado = []

    for i in range(n):
        x = float(v[i]) - float(u[i])
        resultado.append(f"{x:.2f}")

    print(" ".join(resultado))

    n = int(input())
