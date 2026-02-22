n = int(input())

eh_superior = True
eh_inferior = True

for i in range(n):
    linha = list(map(int, input().split()))
    for j in range(n):
        if i > j and linha[j] != 0:
            eh_superior = False
        if i < j and linha[j] != 0:
            eh_inferior = False

if eh_superior and eh_inferior:
    print("SIM: DIAGONAL")
elif eh_superior:
    print("SIM: SUPERIOR")
elif eh_inferior:
    print("SIM: INFERIOR")
else:
    print("NAO")
