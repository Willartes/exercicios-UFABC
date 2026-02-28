total_homens = 0
total_mulheres = 0
soma_altura_homens = 0.0
soma_peso_mulheres = 0.0

idades = []
alturas = []
pesos = []
generos = []

for i in range(100):
    idade = int(input())
    altura = float(input())
    peso = float(input())
    genero = input().strip()

    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    generos.append(genero)

    if genero == 'M':
        total_homens += 1
        soma_altura_homens += altura
    else:  # genero == 'F'
        total_mulheres += 1
        soma_peso_mulheres += peso

# Cálculo das médias (se houver alguém em cada categoria)
if total_homens > 0:
    media_altura_homens = soma_altura_homens / total_homens
else:
    media_altura_homens = 0.0

if total_mulheres > 0:
    media_peso_mulheres = soma_peso_mulheres / total_mulheres
else:
    media_peso_mulheres = 0.0

homens_acima_media_altura = 0
mulheres_abaixo_media_peso = 0

for i in range(100):
    if generos[i] == 'M':
        if total_homens > 0 and alturas[i] > media_altura_homens:
            homens_acima_media_altura += 1
    else:  # 'F'
        if total_mulheres > 0 and pesos[i] < media_peso_mulheres:
            mulheres_abaixo_media_peso += 1


if total_homens == 0:
    print("Nao houve entrada de atletas homens.")
else:
    print("Ha", homens_acima_media_altura,
          "atletas homens acima da media da altura dos homens.")

if total_mulheres == 0:
    print("Nao houve entrada de atletas mulheres.")
else:
    print("Ha", mulheres_abaixo_media_peso,
          "atletas mulheres abaixo da media do peso das mulheres.")

