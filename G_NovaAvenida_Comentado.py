# Leitura das dimensões da matriz: N (linhas) e M (colunas)
N, M = map(int, input().split())

# Inicializa a matriz vazia
matriz = []

# Loop para ler as N linhas da matriz
for _ in range(N):
    # Lê uma linha, converte os valores para inteiros e armazena em uma lista
    linha = list(map(int, input().split()))
    # Adiciona a linha à matriz
    matriz.append(linha)

# Inicializa a variável que armazenará o menor valor com infinito
# Isso garante que qualquer valor encontrado será menor
menor_valor = float('inf')

# Percorre cada coluna (avenida) da matriz
for j in range(M):
    # Inicializa a soma dos valores da coluna atual
    soma_avenida = 0
    
    # Percorre todas as linhas para somar os valores da coluna j
    for i in range(N):
        soma_avenida += matriz[i][j]  # Acumula o valor da célula [i][j]
    
    # Se a soma desta coluna for menor que o menor valor encontrado até agora
    if soma_avenida < menor_valor:
        # Atualiza o menor valor
        menor_valor = soma_avenida

# Imprime o menor valor encontrado entre todas as colunas
print(menor_valor)