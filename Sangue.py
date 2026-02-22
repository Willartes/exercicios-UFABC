line = input().split()
paciente = line[0]
doador = line[1]

compativel = False

if paciente == 'AB':
    compativel = True
elif paciente == 'A':
    if doador == 'A' or doador == 'O':
        compativel = True
elif paciente == 'B':
    if doador == 'B' or doador == 'O':
        compativel = True
elif paciente == 'O':
    if doador == 'O':
        compativel = True

if compativel:
    print("transfusao compativel")
else:
    print("transfusao incompativel")
