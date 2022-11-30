print('DIGITE OS LADOS DO TRIANGULO')
lado_1 = float(input('Digite o primeiro lado: '))
lado_2 = float(input('Digite o segundo lado: '))
lado_3 = float(input('Digite o terceiro lado: '))
tipo = ''
if (lado_1 + lado_2) > lado_3 and (lado_1 + lado_3) > lado_2 and (lado_2 + lado_3) > lado_1:
    if lado_1 == lado_2 == lado_3:
        tipo = 'Equilátero'
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
else:
    tipo = 'INVALIDO'

print(f'O tipo do triangulo digitado é: {tipo}')