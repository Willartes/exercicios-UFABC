def primo(numero):
    soma = 0
    for i in range(1, numero + 1):    
        if numero % i == 0:
            soma += 1
    if soma == 2:
        return True
    else:
        return False

while True:
    N = int(input())

    if N < 0:
        break

    ehPrimo = primo(N)

    if ehPrimo:
        print("SIM")
    else:
        print("NAO")