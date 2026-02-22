while True:
    try:
        linha = input()

        palavras = linha.split('-')
        if not linha:
            break

        alvo ="COBOL"

        eh_cobol = True

        if len(palavras) != 5:
            eh_cobol = False

        else:
            for i in range(5):
                palavra_atual = palavras[i]
                letra_esperada = alvo[i]

                primeira_letra = palavra_atual[0].upper()

                ultima_letra = palavra_atual[-1].upper()

                if primeira_letra == letra_esperada or ultima_letra == letra_esperada:
                    continue
                else:
                    eh_cobol = False
                    break


        if eh_cobol:
            print("GRACE HOPPER")
        else:
            print("BUG")
        
    except EOFError:
        break


