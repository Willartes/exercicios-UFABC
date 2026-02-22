N = int(input())

lista_soma = []

while N > 0:
    
    M = int(input())
    soma = 0
    while M > 0:
        numero = int(input())

        soma += numero
        M -= 1
    lista_soma.append(soma)
    N -= 1


for resultado in lista_soma:
    print(resultado)
    

