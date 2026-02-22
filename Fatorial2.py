def gerar_fatorial(numero):
    fatorial = 1

    while numero > 0:
        fatorial *= numero
        numero -= 1
    return fatorial

while True:
    N = int(input())

    if N < 0:
        break

    resultado = gerar_fatorial(N)

    print(resultado)