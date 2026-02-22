while True:
    try:
        # Tenta ler a entrada. O strip() remove espaços em branco extras (como o \n)
        palavra = input().strip()

        # Se a entrada for vazia (apenas enter), continua para a próxima iteração
        if not palavra:
            continue

        # Definição das vogais
        vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        # Lista para armazenar as letras que NÃO são vogais (consoantes/outros)
        palavra_sem_vogais_lista = []

        # Contador de vogais removidas
        contador_vogais = 0

        # Itera sobre cada letra da palavra lida
        for letra in palavra:
            if letra in vogais:
                # Se for vogal, incrementa o contador
                contador_vogais += 1
            else:
                # Se não for vogal, adiciona na lista de caracteres permitidos
                palavra_sem_vogais_lista.append(letra)

        # Junta a lista de caracteres de volta em uma string
        resultado_palavra = "".join(palavra_sem_vogais_lista)

        # Imprime no formato: "Quantidade PalavraSemVogais"
        print(f"{contador_vogais} {resultado_palavra}")
        
    except EOFError:
        # Encerra o loop quando o final do arquivo (EOF) é detectado
        break
