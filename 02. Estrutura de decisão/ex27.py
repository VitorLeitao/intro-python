fruta = input('Digite a fruta desejada[MAÇA - M / MORANGO - MO]: ').upper()
quantidade = float(input('Digite a quantidade(Kg): '))
if fruta == 'M':
    if quantidade <= 5:
        valor_kg = 1.8
    else:
        valor_kg = 1.5

if fruta == 'MO':
    if quantidade <= 5:
        valor_kg = 2.5
    else:
        valor_kg = 2.2

valor = quantidade * valor_kg
if valor > 25 or quantidade > 8:
    valor = valor * 0.9

print(f'O valor a ser pago é: {valor}')