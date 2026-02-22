import sys

# Dicionário de mapeamento direto das letras para números
# Isso facilita a conversão sem precisar de muitos 'if/elif'
mapa = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
}

# Loop para ler todas as linhas da entrada padrão (sys.stdin)
# Isso resolve a questão do EOF automaticamente
for linha in sys.stdin:
    resultado = ""

    # Percorre cada caractere da linha lida
    for char in linha:
        # Converte para maiúscula para facilitar a busca no mapa
        char_upper = char.upper()

        if char_upper in mapa:
            # Se for letra, adiciona o número correspondente
            resultado += mapa[char_upper]
        elif char.isdigit():
            # Se for dígito (0-9), adiciona diretamente
            resultado += char
        elif char == '*' or char == '#':
            # Se for símbolo permitido, adiciona
            resultado += char
        # Qualquer outro caractere é ignorado (não faz nada)

    # Imprime o resultado da linha processada
    print(resultado)
