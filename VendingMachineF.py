import sys

entrada_bruta = sys.stdin.read().split()
if entrada_bruta:
    fluxo_dados = iter(entrada_bruta)
    
    while True:
        try:
            valor_objetivo = int(next(fluxo_dados))
            if valor_objetivo == 0:
                break
            
            total_moedas = int(next(fluxo_dados))
            lista_moedas = [int(next(fluxo_dados)) for _ in range(total_moedas)]
            
            bits_alcancaveis = 1
            bit_alvo = 1 << valor_objetivo
            mascara_bits = (1 << (valor_objetivo + 1)) - 1
            
            foi_possivel = False
            
            for quantidade in range(1, valor_objetivo + 1):
                proximos_bits = 0
                for valor_moeda in lista_moedas:
                    proximos_bits |= (bits_alcancaveis << valor_moeda)
                
                bits_alcancaveis = proximos_bits & mascara_bits
                
                if bits_alcancaveis & bit_alvo:
                    sys.stdout.write(str(quantidade)+"\n")
                    foi_possivel = True
                    break
                
                if bits_alcancaveis == 0:
                    break
            
            if not foi_possivel:
                sys.stdout.write("impossivel\n")
                
        except StopIteration:
            break