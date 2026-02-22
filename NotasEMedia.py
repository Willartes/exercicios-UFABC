i = 1
soma = 0

while i <= 10:
    print(f"Informe a {i}a. nota:")
    N = float(input())
    i += 1
    soma += N

media = soma/10

print(f"Sua Media Final dos Trabalhos (NFT) foi {media:.2f}")


