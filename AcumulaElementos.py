while True:
    linha = input().strip()
    while linha == "":
        linha = input().strip()
    N = int(linha)
    if N == 0:
        break

    v = list(map(int, input().split()))

    maior = v[0]
    i = 1
    while i < N:
        if v[i] > maior:
            maior = v[i]
        i += 1

    freq = [0] * (maior + 1)

    i = 0
    while i < N:
        freq[v[i]] += 1
        i += 1

    i = 1
    while i <= maior:
        freq[i] += freq[i - 1]
        i += 1

    i = 0
    while i <= maior:
        print("[" + str(i) + "] " + str(freq[i]))
        i += 1

