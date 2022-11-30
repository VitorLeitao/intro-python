lista = []
for c in range(0, 3):
    num = float(input('Digite um numero: '))
    lista.append(num)

if lista[0] <= lista[1] <= lista[2]:
    crescente = f'{lista[2]}, {lista[1]}, {lista[0]}'
if lista[0] <= lista[2] <= lista[1]:
    crescente = f'{lista[1]}, {lista[2]}, {lista[0]}'

if lista[1] <= lista[0] <= lista[2]:
    crescente = f'{lista[2]}, {lista[0]}, {lista[1]}'
if lista[1] <= lista[2] <= lista[0]:
    crescente = f'{lista[0]}, {lista[2]}, {lista[1]}'

if lista[2] <= lista[0] <= lista[1]:
    crescente = f'{lista[1]}, {lista[0]}, {lista[2]}'
if lista[2] <= lista[1] <= lista[0]:
    crescente = f'{lista[0]}, {lista[1]}, {lista[2]}'


print(crescente)
