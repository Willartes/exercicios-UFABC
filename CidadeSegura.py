N = int(input())
linha_anterior = list(map(int, input().split()))
dp_col = [0]*(N+1)
for i in range(N):
    linha_atual = list(map(int, input().split()))
    for j in range(N+1):
        dp_col[j] = linha_anterior[j] + linha_atual[j]
    linha_saida = []
    for j in range(N):
        total = dp_col[j] + dp_col[j+1]
        if total >= 2:
            linha_saida.append('S')
        else:
            linha_saida.append('U')
    print(''.join(linha_saida))
    linha_anterior = linha_atual
