entrada = input().split()

soma = 0

for item in entrada:
    N = int(item)

    if N == 0:
        break

    soma += N

print(soma)
