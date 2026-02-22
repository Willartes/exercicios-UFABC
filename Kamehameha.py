N = int(input())

while N > 0:
    texto = input()
    
    quantidade = len(texto) - 7

    resultado = texto + 'h' + ('a' * quantidade)
    
    print(resultado)

    N -= 1