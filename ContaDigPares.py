while True:
    try:
        linha = input()
    except EOFError:
        break

    n = linha.strip()
    if n == "":
        continue

    cont = 0
    for d in n:
        if d in "02468":
            cont += 1

    print(cont)
