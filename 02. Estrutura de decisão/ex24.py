import math
num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
operador = input('Digite o operador[+ - x %]: ')
if operador == '+' or operador == '-' or operador == 'x' or operador == '%':
    if operador == '+':
        resultado = num_1 + num_2
    if operador == '-':
        resultado = num_1 - num_2
    if operador == 'x':
        resultado = num_1 * num_2
    if operador == '%':
        resultado = num_1 / num_2

    print(f'O resultado é: {resultado}')
    print('informações:')

    if resultado % 2 == 0:
        print(f'{resultado} é par.')
    else:
        print(f'{resultado} é impar.')

    if resultado >= 0:
        print(f'{resultado} é positivo.')
    else:
        print(f'{resultado} é negativo.')

    if  resultado == math.floor(resultado):
        print(f'{resultado} é inteiro.')
    else:
        print(f'{resultado} é decimal.')

else:
    print('Operador INVALIDO.')