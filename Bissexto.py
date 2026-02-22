ano = eval(input())

if ano % 400 == 0:
    print("ANO BISSEXTO")
elif ano % 100 == 0:
    print("ANO NAO BISSEXTO")
elif ano % 4 == 0:
    print("ANO BISSEXTO")
else:
    print("ANO NAO BISSEXTO")