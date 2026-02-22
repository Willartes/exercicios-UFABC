N = int(input())

fatorial = 1

while N > 0:
    fatorial *= N
    N -= 1

print(fatorial)