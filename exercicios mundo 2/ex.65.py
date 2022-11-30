l1 = 0
l2 = 's'
while l2 == 's':
    l3 = float(input('digite um numero: '))
    if l1 == 0:
        maior = l3
        menor = l3
    else:
        if l3 > maior:
            maior = l3
        if l3 < menor:
            menor = l3
    l1 = l1 + 1
    l2 = input('deseja continuar digitando? [S/N]').strip().lower()
print('o maior numero foi:{}'.format(maior))
print('o menor numero foi {}'.format(menor))