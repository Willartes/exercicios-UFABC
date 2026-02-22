while True:
    try:
        primeira_palavra, segunda_palavra = map(str, input().split())

        
        if not (primeira_palavra and segunda_palavra):
            break

        alvo = primeira_palavra

        eh_igual = True

        if len(alvo) != len(segunda_palavra):
            eh_igual = False

        else:
            for i in range(len(alvo)):
                letra_atual = segunda_palavra[i]
                letra_esperada = alvo[i]

                segunda_letra = letra_atual[0]

                

                if segunda_letra == letra_esperada or primeira_palavra == letra_esperada:
                    continue
                else:
                    eh_igual = False
                    break


        if eh_igual:
            print("iguais")
        else:
            print("diferentes")
        
    except EOFError:
        break


