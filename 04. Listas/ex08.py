idades = []
alturas = []
for c in range(0, 5):
    idade = int(input(f'Digite a {c + 1} idade: '))
    altura = float(input(f'Digite a {c + 1} altura: '))
    idades.append(idade)
    alturas.append(altura)

idades_inversa = []
alturas_inversa = []
for c in range(len(idades) - 1, -1, -1):
    idades_inversa.append(idades[c])
    alturas_inversa.append(alturas[c])

print(idades_inversa)
print(alturas_inversa)