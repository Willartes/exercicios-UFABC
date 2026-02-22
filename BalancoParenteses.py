import sys

for linha in sys.stdin:
    
    expressao = linha.strip()

    
    if not expressao:
        continue

    contador = 0
    esta_correto = True  

    for caractere in expressao:
        if caractere == '(':
            contador += 1
        elif caractere == ')':
            contador -= 1

        
        if contador < 0:
            esta_correto = False
            break  

    
    if esta_correto and contador == 0:
        print("correct")
    else:
        print("incorrect")
