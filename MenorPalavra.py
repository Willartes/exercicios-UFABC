lista_palavras = []
while True:
    try:
        palavra = input()
        if not palavra:
            break
        lista_palavras.append(palavra)
        
    except EOFError:
        break


if not lista_palavras:
    print("Nenhuma palavra foi informada")

else:
    menor_palavra = min(lista_palavras, key= len)
    print(f"A menor palavra informada foi {menor_palavra}")
