area = float(input('digite a area a ser pintada: '))
cobertura_lata = 108
cobertura_galao = 21.6
preco_lata = 80
preco_galao = 25

# Situação A
qt_lata = area / cobertura_lata
if qt_lata % 2 != 0:
    qt_lata = (area // cobertura_lata) + 1
preco_a = qt_lata * preco_lata

# Situação B
qt_galao = area / cobertura_galao
if qt_galao % 2 != 0:
    qt_galao = (area // cobertura_galao) + 1
preco_b = qt_galao * preco_galao

# Situação C
qt_lata_final = area // cobertura_lata
area_sobra = area - (qt_lata_final * cobertura_lata)
qt_galao_final = area_sobra / cobertura_galao
if qt_galao_final % 2 != 0:
    qt_galao_final = (area_sobra // cobertura_galao) + 1
preco_final = (qt_lata_final * preco_lata) + (qt_galao_final * preco_galao)

print(f'A) Comprar apenas {qt_lata} latas de tinta: R${preco_a}')
print(f'B) Comprar apenas {qt_galao} galões de tinta: R${preco_b}')
print(f'C) Comprar {qt_lata_final} latas de tinta e {qt_galao_final} galões de tinta: R${preco_final}')