def validar_Datas(D, M, A):

    if A < 1582:
        return "DATA INVALIDA"
    elif A == 1582 and M < 10:
        return "DATA INVALIDA"
    elif A == 1582 and M == 10 and D < 15:
        return "DATA INVALIDA"
    else:
        
        bissexto = False
        if A % 400 == 0:
            bissexto = True
        elif A % 100 == 0:
            bissexto = False
        elif A % 4 == 0:
            bissexto = True

        
        if M < 1 or M > 12:
            return "DATA INVALIDA"
        else:
            
            meses31 = [1, 3, 5, 7, 8, 10, 12]
            meses30 = [4, 6, 9, 11]

            
            valida = False

            if M in meses31:
                if D >= 1 and D <= 31:
                    valida = True
            elif M in meses30:
                if D >= 1 and D <= 30:
                    valida = True
            elif M == 2:
                if bissexto:
                    if D >= 1 and D <= 29:
                        valida = True
                else:
                    if D >= 1 and D <= 28:
                        valida = True

            if valida:
                return "DATA VALIDA"
            else:
                return "DATA INVALIDA"

N = int(input())

contador = 1

while contador <= N:
    D, M, A = map(int, input().split())

    data = validar_Datas(D, M, A)

    print(data)

    contador += 1