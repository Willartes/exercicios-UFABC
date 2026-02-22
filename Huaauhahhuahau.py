# Lê a entrada (a risada)
risada = input()

# Define quais caracteres são vogais
vogais_definidas = "aeiou"

# Variável para guardar apenas as vogais da risada
apenas_vogais = ""

# Percorre cada letra da risada original
for letra in risada:
    # Se a letra for uma vogal, adiciona na variável acumuladora
    if letra in vogais_definidas:
        apenas_vogais = apenas_vogais + letra

# Inverte a string de vogais usando fatiamento (slicing)
vogais_invertidas = apenas_vogais[::-1]

# Compara se a sequência de vogais é igual de trás para frente
if apenas_vogais == vogais_invertidas:
    print("S")
else:
    print("N")
