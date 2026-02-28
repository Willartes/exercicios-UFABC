linha = input().split()
N = int(linha[0])
M = int(linha[1])

# Vetor de diferenças (1..N), vamos usar índices até N+1 com segurança
V = [0] * (N + 2)

# Lê M operações
for _ in range(M):
    op = input().split()
    A = int(op[0])
    B = int(op[1])
    K = int(op[2])

    # Se o problema define A e B como 1-based
    V[A] += K
    if B + 1 <= N:
        V[B + 1] -= K
    # Se B == N, não precisamos mexer em V[N+1] para o cálculo de 1..N

# Agora percorre de 1 a N acumulando e achando o máximo
acumulado = 0
maior = 0

for i in range(1, N + 1):
    acumulado += V[i]
    if acumulado > maior:
        maior = acumulado

print(maior)
