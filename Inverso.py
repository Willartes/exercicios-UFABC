lista_palavras = []
while True:
    try:
        palavra = input()
        if not palavra:
            break
        lista_palavras.append(palavra)
        
    except EOFError:
        break

for item in lista_palavras:
    palavra_invertida = item[::-1]
    print(palavra_invertida)
