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
    maior_palavra = max(lista_palavras, key= len)
    print(f"A maior palavra informada foi {maior_palavra}")
