Id1 = eval(input())
Id2 = eval(input())

if Id1 >= 0 and Id2 <= 1000 and Id1 != Id2:
    validado = True

if validado and Id1 > Id2:
    print(Id1)
else:
    print(Id2)

