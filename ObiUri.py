n = input()

linha = input()

palavras = linha.split()

resultado = []

for palavra in palavras:
    if len(palavra) == 3:

        if palavra[0] == 'O' and palavra[1] == 'B':
            resultado.append('OBI')

        elif palavra[0] == 'U' and palavra[1] == 'R':
            resultado.append('URI')

        else:
            resultado.append(palavra)
    else:

        resultado.append(palavra)

print(" ".join(resultado))
