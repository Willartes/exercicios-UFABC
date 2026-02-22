# Leitura até EOF
while True:
    try:
        dna = input().strip()
    except EOFError:
        break

    rna = ""

    # Para cada caractere do DNA, montamos o RNAm
    for base in dna:
        if base == 'C':
            rna += 'G'
        elif base == 'G':
            rna += 'C'
        elif base == 'T':
            rna += 'A'
        elif base == 'A':
            rna += 'U'

    print(rna)
