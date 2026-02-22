N = int(input())

letras = input()

direcoes = ['N', 'L','S', 'O']


indice = 0


for i in letras:
    if i == 'D':
        indice = indice + 1
    elif i == 'E':
        indice = indice - 1    

direcao = direcoes[indice % 4]

print(direcao)