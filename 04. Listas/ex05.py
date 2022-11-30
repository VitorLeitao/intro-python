lista_total = []
lista_pares = []
lista_impares = []
for c in range(1, 6):
    num = int(input(f'Digite o {c}° numero inteiro: '))
    lista_total.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(f'Vetor total: {lista_total}')
print(f'Vetor pares: {lista_pares}')
print(f'Vetor impares: {lista_impares}')