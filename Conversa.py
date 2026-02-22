# Lê o número de casos de teste
try:
    line = input()
    if line:
        numero_casos = int(line)
    else:
        numero_casos = 0
except EOFError:
    numero_casos = 0

for i in range(numero_casos):
    try:
        line = input()
        if not line:
            break
        numero_pessoas = int(line)

        lista_idioma = []

        # Lê os idiomas das pessoas do grupo
        for j in range(numero_pessoas):
            idioma = input()
            if not idioma:
                break
            lista_idioma.append(idioma)

        # Define o primeiro idioma como referência
        idioma_alvo = lista_idioma[0]
        eh_igual = True

        # Verifica se alguém fala um idioma diferente
        for idioma in lista_idioma:
            if idioma_alvo != idioma:
                eh_igual = False
                break # Se achou um diferente, para de verificar imediatamente

        # A impressão deve ser feita FORA do laço de verificação
        if eh_igual:
            print(idioma_alvo)
        else:
            print("ingles")

    except EOFError:
        break
