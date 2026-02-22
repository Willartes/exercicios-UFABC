def classificar_numero(numero):
    """
    Calcula a soma dos divisores próprios de um número (excluindo ele mesmo)
    e determina se ele é abundante, perfeito ou deficiente.

    Parâmetros:
    numero (int): O número inteiro a ser analisado.

    Retorna:
    str: "abundante" se a soma dos divisores > numero.
         "perfeito" se a soma dos divisores == numero.
         "deficiente" se a soma dos divisores < numero.
    """
    soma_divisores = 0

    # Iniciamos a busca por divisores a partir de 1
    divisor = 1

    # Otimização: Não precisamos testar números maiores que a metade do número,
    # pois o maior divisor próprio possível de N é N/2.
    while divisor <= numero // 2:

        # O operador % (módulo) verifica o resto da divisão.
        # Se o resto for 0, 'divisor' divide 'numero' exatamente.
        if numero % divisor == 0:
            soma_divisores += divisor

        divisor += 1

    # Classificação baseada na comparação entre a soma e o número original
    if soma_divisores > numero:
        return "abundante"
    elif soma_divisores == numero:
        return "perfeito"
    else:
        return "deficiente"

# Lista para armazenar os resultados e imprimi-los todos de uma vez no final
resultados = []

while True:
    try:
        # Lê uma linha da entrada padrão
        linha = input()

        # Se a linha estiver vazia (pode acontecer em alguns ambientes de teste), para o loop
        if not linha: 
            break

        N = int(linha)
    except EOFError:
        # EOFError ocorre quando não há mais dados para ler (End Of File)
        break

    # Verifica a condição de parada especificada no problema (-1)
    if N == -1:
        break

    # Chama a função de classificação e guarda o resultado na lista
    resultados.append(classificar_numero(N))

# Itera sobre a lista de resultados acumulados e imprime cada um
for resultado in resultados:
    print(resultado)
