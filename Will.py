while True:
    try:
        alfabeto = input().strip()
    except EOFError:
        break

    
    n = int(input())

    # Lê a linha com os índices das lâmpadas piscadas
    linha_indices = input().split()

    mensagem = ""

    # Para cada índice, converte para inteiro, ajusta para índice de string e pega a letra
    for x in linha_indices:
        lampada = int(x)           # número da lâmpada (1 a 26)
        letra = alfabeto[lampada - 1]
        mensagem += letra

    print(mensagem)
