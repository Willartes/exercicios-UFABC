M, F = map(eval, input().split())

if M >= 6.0 and F <= 30:
    print("Aprovado!")

elif M < 4.0 or F > 30:
    print("Reprovado!")
else:
    print("Exame Final!")