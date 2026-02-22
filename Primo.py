K = int(input())
soma = 0
for i in range(1, K + 1):    
    if K % i == 0:
        soma += 1
if soma == 2:
    print("PRIMO")
else:
    print("COMPOSTO")
