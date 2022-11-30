lista_notas = [100, 50, 10, 5, 1]
dinheiro = int(input('Quanto dinheiro voce deseja retirar: '))

qt_100 = dinheiro // 100
dinheiro = dinheiro - (qt_100 * 100)
qt_50 = dinheiro // 50
dinheiro = dinheiro - (qt_50 * 50)
qt_10 = dinheiro // 10
dinheiro = dinheiro - (qt_10 * 10)
qt_5 = dinheiro // 5
dinheiro = dinheiro - (qt_5 * 5)
qt_1 = dinheiro

qt_notas = [qt_100, qt_50, qt_10, qt_5, qt_1]
for c in range(0, 5):
    if qt_notas[c] > 0:
        print(f'Notas de {lista_notas[c]}: {qt_notas[c]}')
