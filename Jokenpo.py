try:
    casos_teste = int(input())
except (EOFError, ValueError):
    casos_teste = 0

for _ in range(casos_teste):
    try:
        entrada = input().split()
        jogador1 = entrada[0]
        jogador2 = entrada[1]
    except (EOFError, IndexError):
        break

    if jogador1 == jogador2:
        print("empate")
    elif (jogador1 == "tesoura" and jogador2 == "papel") or \
         (jogador1 == "papel" and jogador2 == "pedra") or \
         (jogador1 == "pedra" and jogador2 == "tesoura"):
        print("jogador 1")
    else:
        print("jogador 2")
