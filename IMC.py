A, P = map(eval, input().split())

imc = P/pow(A, 2)

if imc < 16:
    print("Magreza grave")
elif 16 <= imc < 17:
    print("Magreza moderada")
elif 17<= imc < 18.5:
    print("Magreza leve")
elif 18.5 <= imc < 25:
    print("Saudavel")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade Grau I")
elif 35 <= imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (morbida)")