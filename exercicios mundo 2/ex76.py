lista = ('monitor', 400, 'mouse', 100, 'teclado', 200, 'fone', 90)
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for c in range(0, 7, 2):
    print(f'{lista[c]:.<30} R${lista[c + 1]}')