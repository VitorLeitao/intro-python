lista = []
for c in range(0, 5):
    lista.append(int(input('digite um numero: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
        posi_menor = len(lista)
        posi_maior = len(lista)
    else:
        if lista[c] > maior:
            maior = lista[c]
            posi_maior = len(lista)
        if lista[c] < menor:
            menor = lista[c]
            posi_menor = len(lista)

print(f'o maior numero pe {maior} e ele esta na posição {posi_maior - 1}')
print(f'o menor numnero é {menor} e ele esta na posição {posi_menor - 1}')