"""
Objetivo (inferido):
Ler uma data (D M A) e, se ela for válida no calendário Gregoriano (a partir de
15/10/1582), imprimir a data do dia seguinte no formato "DD MM AAAA".

Abaixo está a versão DOCUMENTADA e COMENTADA mantendo a intenção.
"""

# Lê três inteiros da entrada: dia (D), mês (M) e ano (A).
D, M, A = map(int, input().split())

# --- 1) Regras de corte: apenas datas no calendário Gregoriano ---
# O calendário Gregoriano começou em 15/10/1582.
# Portanto, qualquer data anterior é considerada inválida (o código original "passa" e não imprime nada).
if A < 1582:
    pass
elif A == 1582 and M < 10:
    pass
elif A == 1582 and M == 10 and D < 15:
    pass
else:
    # --- 2) Funções auxiliares ---

    def bissexto(ano: int) -> bool:
        """
        Retorna True se 'ano' for bissexto no calendário Gregoriano, caso contrário False.

        Regra:
        - Divisível por 400 => bissexto
        - Divisível por 100 (mas não por 400) => não bissexto
        - Divisível por 4 (mas não por 100) => bissexto
        - Caso contrário => não bissexto
        """
        if ano % 400 == 0:
            return True
        elif ano % 100 == 0:
            return False
        elif ano % 4 == 0:
            return True
        return False

    def dias_no_mes(mes: int, ano: int) -> int:
        """
        Devolve o número de dias do 'mes' no 'ano'.
        Retorna 0 se o mês for inválido (fora de 1..12).
        """
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        elif mes == 2:
            return 29 if bissexto(ano) else 28
        return 0

    # --- 3) Validação de mês ---
    # Se o mês não estiver entre 1 e 12, a data é inválida e nada é impresso.
    if M < 1 or M > 12:
        pass
    else:
        # --- 4) Validação de dia ---
        # Calcula o limite de dias do mês/ano informados.
        max_dias = dias_no_mes(M, A)

        # Se o dia não estiver no intervalo válido, a data é inválida.
        if D < 1 or D > max_dias:
            pass
        else:
            # --- 5) Cálculo do dia seguinte ---
            # Começa avançando 1 no dia e, se "estourar" o mês, ajusta mês e ano.
            Ds = D + 1   # dia seguinte
            Ms = M       # mês seguinte (inicialmente igual)
            As = A       # ano seguinte (inicialmente igual)

            # Se o novo dia exceder o número de dias do mês atual, vira o 1º do próximo mês.
            if Ds > dias_no_mes(M, A):
                Ds = 1
                Ms += 1

                # Se o mês exceder 12, vira janeiro e incrementa o ano.
                if Ms > 12:
                    Ms = 1
                    As += 1

            # --- 6) Saída formatada ---
            # {Ds:02d} e {Ms:02d} imprimem dia e mês com 2 dígitos (ex.: 03, 11).
            print(f"{Ds:02d} {Ms:02d} {As}")
