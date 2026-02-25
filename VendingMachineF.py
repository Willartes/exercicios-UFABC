while True:
    try:
        linha_configuracao = input().split()
        if not linha_configuracao:
            break
            
        valor_troco_alvo = int(linha_configuracao[0])
        if valor_troco_alvo == 0:
            break
            
        total_tipos_moedas = int(linha_configuracao[1])
        
        lista_de_moedas = []
        while len(lista_de_moedas) < total_tipos_moedas:
            lista_de_moedas.extend(map(int, input().split()))
        
        combinacoes_bits = 1
        bit_objetivo = 1 << valor_troco_alvo
        mascara_limite = (1 << (valor_troco_alvo + 1)) - 1
        
        sucesso = False

        for quantidade_moedas in range(1, valor_troco_alvo + 1):
            novas_combinacoes = 0
            for valor_moeda in lista_de_moedas:
                novas_combinacoes |= (combinacoes_bits << valor_moeda)
            
            combinacoes_bits = novas_combinacoes & mascara_limite
            
            if combinacoes_bits & bit_objetivo:
                print(quantidade_moedas)
                print()
                sucesso = True
                break
            
            if combinacoes_bits == 0:
                break
        
        if not sucesso:
            print("impossivel")
            
    except EOFError:
        break