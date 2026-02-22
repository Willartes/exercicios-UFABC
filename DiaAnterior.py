"""
UFABC - O DIA ANTERIOR

Objetivo:
Receber uma data válida do calendário Gregoriano e imprimir a data do dia anterior,
também segundo as regras do calendário Gregoriano.

Regras de saída:
- Da e Ma sempre com 2 dígitos
- Aa sempre com 4 dígitos
- Se não existir dia anterior no calendário Gregoriano (antes de 15/10/1582),
  imprimir exatamente:
  "nao existe dia anterior para esta data"
"""

# Leitura de entrada: dia, mês, ano
D, M, A = map(int, input().split())

# ------------------------------------------------------------
# Validação do "início" do calendário Gregoriano:
# A primeira data considerada é 15/10/1582.
# Logo, para 15/10/1582 não existe "dia anterior" definido no Gregoriano
# (assim como para qualquer data anterior a ela).
# ------------------------------------------------------------
if A < 1582 or (A == 1582 and (M < 10 or (M == 10 and D <= 15))):
    print("nao existe dia anterior para esta data")
else:
    # --------------------------------------------------------
    # Função: verifica se o ano é bissexto no calendário Gregoriano
    # --------------------------------------------------------
    def bissexto(ano: int) -> bool:
        """Retorna True se 'ano' for bissexto no calendário Gregoriano."""
        if ano % 400 == 0:
            return True
        if ano % 100 == 0:
            return False
        return ano % 4 == 0

    # --------------------------------------------------------
    # Função: retorna quantos dias tem o mês 'mes' no ano 'ano'
    # (corrigindo a tabela de meses, sem mudar a ideia da lógica original)
    # --------------------------------------------------------
    def dias_no_mes(mes: int, ano: int) -> int:
        """Retorna o número de dias do mês 'mes' no 'ano' (Gregoriano)."""
        if mes in (1, 3, 5, 7, 8, 10, 12):
            return 31
        if mes in (4, 6, 9, 11):
            return 30
        if mes == 2:
            return 29 if bissexto(ano) else 28
        return 0  # mês inválido (não deve ocorrer, pois a entrada é dita válida)

    # --------------------------------------------------------
    # As checagens abaixo existiam no código original (com "pass").
    # Como a especificação diz que a entrada é uma data válida,
    # mantemos a lógica (não criamos novos fluxos), apenas organizamos.
    # --------------------------------------------------------
    if M < 1 or M > 12:
        pass
    else:
        max_dias = dias_no_mes(M, A)

        if D < 1 or D > max_dias:
            pass
        else:
            # --------------------------------------------
            # Cálculo do dia anterior:
            # 1) Tenta apenas D-1 no mesmo mês/ano
            # 2) Se "estourar" (Da < 1), volta para o último dia do mês anterior
            # --------------------------------------------
            Da = D - 1
            Ma = M
            Aa = A

            if Da < 1:
                # Vai para o mês anterior
                Ma -= 1
                if Ma < 1:
                    # Volta para dezembro do ano anterior
                    Ma = 12
                    Aa -= 1

                # Agora sim: último dia do mês (já ajustado) no ano (já ajustado)
                Da = dias_no_mes(Ma, Aa)

            # Saída com formatação exigida: DD MM AAAA
            print(f"{Da:02d} {Ma:02d} {Aa:04d}")
