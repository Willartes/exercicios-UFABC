# Lê o número de palavras (embora em Python possamos ler a linha inteira direto)
n = input()

# Lê a linha contendo todas as palavras separadas por espaço
linha = input()

# Divide a linha em uma lista de palavras
palavras = linha.split()

# Lista para guardar as palavras corrigidas
resultado = []

for palavra in palavras:
    # Verifica se a palavra tem exatamente 3 letras
    if len(palavra) == 3:
        # Verifica se começa com 'OB'
        if palavra[0] == 'O' and palavra[1] == 'B':
            resultado.append('OBI')
        # Verifica se começa com 'UR'
        elif palavra[0] == 'U' and palavra[1] == 'R':
            resultado.append('URI')
        # Se não for nenhum dos casos acima, mantém a palavra original
        else:
            resultado.append(palavra)
    else:
        # Se não tiver 3 letras, mantém a palavra original
        resultado.append(palavra)

# Junta as palavras corrigidas com espaço e imprime
print(" ".join(resultado))
