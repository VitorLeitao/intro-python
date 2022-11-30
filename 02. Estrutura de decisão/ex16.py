import math


print('Função de segundo grau: ax2 + bx + c.')
a = float(input('Digite o valor de A: '))
if a != 0:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print('A equação nao tem raizes.')
    else:
        if delta == 0:
            raiz = (b * -1) / (2 * a)
            print(f'A raiz da equação é: {raiz}')
        else:
            raiz_1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
            raiz_2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
            print(f'As raizes da equação são: {raiz_1} e {raiz_2}.')
else:
    print('A equação nao é do segundo grau.')

