tipo = input('Digite o tipo de carne dentre as opções\nFile Duplo - F\nAlcatra - A\nPicanha - P\nResposta: ').upper()
quantidade = float(input('Digite a quantidade de carne(Kg): '))
pagamento = input('A compra será no cartão[S/N]: ').upper()
if tipo == 'F':
    if quantidade <= 5:
        valor_kg = 4.9
    else:
        valor_kg = 5.8
if tipo == 'A':
    if quantidade <= 5:
        valor_kg = 5.9
    else:
        valor_kg = 6.8
if tipo == 'P':
    if quantidade <= 5:
        valor_kg = 6.9
    else:
        valor_kg = 7.8

valor = quantidade * valor_kg
if pagamento == 'S':
    valor = 0.95 * valor

print(f'O valor a se pagar é: {valor}')