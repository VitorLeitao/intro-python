lista = []
for c in range(0, 3):
    preco = float(input(f'Digite o preco da {c + 1}° loja: '))
    lista.append(preco)

if lista[0] < lista[1]:
    if lista[0] < lista[2]:
        min = lista[0]
    else:
        min = lista[2]

if lista[1] < lista[0]:
    if lista[1] < lista[2]:
        min = lista[1]
    else:
        min = lista[2]

if lista[0] == lista[1]:
    if lista[0] < lista[2]:
        min = lista[0]
    else:
        min = lista[2]

print(f'O melhor preço é: {min}')