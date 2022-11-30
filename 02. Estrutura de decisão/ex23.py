import math
num = float(input('Digite um numero: '))
arredondado = math.floor(num)

if num == arredondado:
    print('Numero é inteiro.')
else:
    print('O numero NÃO é inteiro.')


