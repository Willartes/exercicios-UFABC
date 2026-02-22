lista_letra = []
while True:
    try:
        letra = input().strip()

        if letra == '*':
            break
        if not letra:
            continue

        lista_letra.append(letra)
    except EOFError:
        break
    
    

vogais = ['a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']
consoantes = []
soma = 0

for item in lista_letra:
    if item.isalpha() and item not in vogais:
        consoantes.append(item)
        soma += 1
print(soma)
