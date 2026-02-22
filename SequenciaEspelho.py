c = int(input())
for _ in range(c):
    linha = input().split()
    b = int(linha[0])
    e = int(linha[1])

    sequencia = ""
    
    for i in range(b, e + 1):
        sequencia += str(i)

    
    invertida = sequencia[::-1]

    print(sequencia + invertida)
