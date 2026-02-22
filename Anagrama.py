# Lê a palavra principal (p1)
palavra_principal = input().strip()

# Lê a quantidade de palavras (N)
try:
    line = input().strip()
    if not line:
        N = 0
    else:
        N = int(line)
except EOFError:
    N = 0

lista_palavras = []

# Lê as N palavras da lista
while N > 0:
    try:
        palavra = input().strip()
        # Se a linha estiver vazia, continua tentando ler até acabar N
        if not palavra: 
            continue
        lista_palavras.append(palavra)
        N -= 1
    except EOFError:
        break

# Variável de controle para saber se achou
encontrou = False

# Verifica cada palavra da lista
for item in lista_palavras:
    # Inverte a palavra atual da lista
    palavra_invertida = item[::-1]

    # Compara se a palavra principal é IGUAL à palavra da lista invertida
    if palavra_principal == palavra_invertida:
        encontrou = True
        break # Se achou um, não precisa continuar procurando

# Saída conforme especificado
if encontrou:
    print("sim")
else:
    print("nao")
