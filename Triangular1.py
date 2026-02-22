n = int(input())

triangular = True

for i in range(n):
    linha = list(map(int, input().split()))
    for j in range(n):
        if i > j and linha[j] != 0:
            triangular = False
if triangular:
    print("SIM")
else:
    print("NAO")
