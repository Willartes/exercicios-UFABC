lista_soma = []

while True:
    try:
        entrada = input().split()
        soma = 0
        for item in entrada:
            N = int(item)

            if N == 0:
                break
            soma += N
        lista_soma.append(soma)

    except EOFError:
        break    
for resultado in lista_soma:
    print(resultado)
