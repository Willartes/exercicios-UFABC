S, F = map(int, input().split())

contador = S
lista_primos = []

while contador <= F:
    soma = 0
    i = 1
    while i <= contador:
        if contador % i == 0:
            soma += 1
        i += 1

    if soma == 2:
        lista_primos.append(contador)

    contador += 1

print(f"Primos entre {S} e {F}:", *lista_primos)
