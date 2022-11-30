tipo = input('Digite o tipo de compustivel[G/A]: ').upper()
quantidade = float(input('Digite o quantidade de litros: '))
if tipo == 'A':
    preco = 1.9
    if quantidade <= 20:
        preco = preco - (0.03 * preco)
        valor = preco * quantidade
    else:
        preco = preco - (0.05 * preco)
        valor = preco * quantidade
    print(f'O valor a se pagar por {quantidade} de litros de alcool é: {valor}')

elif tipo == 'G':
    preco = 2.5
    if quantidade <= 20:
        preco = preco - (preco * 0.04)
        valor = preco * quantidade
    else:
        preco = preco - (preco * 0.06)
        valor = preco * quantidade
    print(f'O valor a se pagar por {quantidade} de litros de gasolina é: {valor}')

else:
    print('Erro na digitação.')


