area = float(input('digite a area a ser pintada: '))
area_lata = 54
valor_lata = 80
qt_latas = area / area_lata
if qt_latas % 2 != 0:
    qt_latas = (area // area_lata) + 1

pagar = qt_latas * valor_lata
print(f'Quantidade de latas: {qt_latas}')
print(f'Preço a se pagar: {pagar}')

