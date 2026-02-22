N = int(input())

notas1 = []
notas2 = []
notas3 = []

# Lê as notas dos N alunos
for _ in range(N):
    linha = input().split()
    g1 = float(linha[0])
    g2 = float(linha[1])
    g3 = float(linha[2])

    notas1.append(g1)
    notas2.append(g2)
    notas3.append(g3)

# Calcula as médias de cada atividade
soma1 = 0.0
soma2 = 0.0
soma3 = 0.0

for i in range(N):
    soma1 += notas1[i]
    soma2 += notas2[i]
    soma3 += notas3[i]

media1 = soma1 / N
media2 = soma2 / N
media3 = soma3 / N

# Conta quantos alunos ficaram abaixo da média em cada atividade
abaixo1 = 0
abaixo2 = 0
abaixo3 = 0

for i in range(N):
    if notas1[i] < media1:
        abaixo1 += 1
    if notas2[i] < media2:
        abaixo2 += 1
    if notas3[i] < media3:
        abaixo3 += 1

print("Na 1a. atividade", abaixo1, "alunos tiveram nota abaixo da media.")
print("Na 2a. atividade", abaixo2, "alunos tiveram nota abaixo da media.")
print("Na 3a. atividade", abaixo3, "alunos tiveram nota abaixo da media.")
