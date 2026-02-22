n = int(input())
for _ in range(n):
    placa = input() 

    
    valida = True

    
    if len(placa) != 8:
        valida = False
    else:
        
        if placa[3] != '-':
            valida = False

     
        if not (placa[0].isupper() and placa[1].isupper() and placa[2].isupper()):
            valida = False
       
        if not (placa[0].isalpha() and placa[0].isupper()): 
            valida = False
    

        if not (placa[4].isdigit() and placa[5].isdigit() and placa[6].isdigit() and placa[7].isdigit()):
            valida = False

    if not valida:
        print("FAILURE")
    else:
        
        ultimo = int(placa[7])
        if ultimo == 1 or ultimo == 2:
            print("MONDAY")
        elif ultimo == 3 or ultimo == 4:
            print("TUESDAY")
        elif ultimo == 5 or ultimo == 6:
            print("WEDNESDAY")
        elif ultimo == 7 or ultimo == 8:
            print("THURSDAY")
        else:
            print("FRIDAY")
