lista = []
for c in range(0, 3):
    num = float(input('Digite um numero: '))
    lista.append(num)

# Determinar o MAIOR
if lista[0] >= lista[1]:
    if lista[0] >= lista[2]:
        max = lista[0]
    else:
        max = lista[2]
if lista[1] > lista[0]:
    if lista[1] >= lista[2]:
        max = lista[1]
    else:
        max = lista[2]

# Determinar o MENOR
if lista[0] <= lista[1]:
    if lista[0] <= lista[2]:
        min = lista[0]
    else:
        min = lista[2]
if lista[1] < lista[0]:
    if lista[1] <= lista[2]:
        min = lista[1]
    else:
        min = lista[2]

print(f'O maior numero é: {max} e o menor é: {min}.')


