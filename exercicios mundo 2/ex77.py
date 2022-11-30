lista = ('lol', 'killua', 'hunter', 'volei', 'zed')
for c in range (0, 5):
    print(f'\nna palavra {lista[c]} temos: ', end = '')
    if 'a' in lista[c]:
        print('a', end = '')
    if 'e' in lista[c]:
        print(' e', end = '')
    if 'i' in lista[c]:
        print(' i', end = '')
    if 'o' in lista[c]:
        print(' o', end = '')
    if 'u' in lista[c]:
        print(' u', end = '')
