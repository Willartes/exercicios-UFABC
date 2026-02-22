
while True:
    try:
        palavra, numero = map(str, input().split())

        numero = int(numero)

        resultado = palavra[numero]

        print(*resultado)
    except EOFError:
        break


