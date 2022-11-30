for c in range(1,6):
    l1 = float(input('digite o peso da {} pessoa'.format(c)))
    if c == 1:
        maior = l1
        menor = l1
    else:
        if l1 > maior:
            maior = l1
        if l1 < menor:
            menor = l1
print('0 maior peso é {}'.format(maior))
print('o mwnoe peso é {}'.format(menor))



