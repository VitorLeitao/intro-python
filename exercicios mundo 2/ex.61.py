print('vamos calcular uma PA!!!')
l1 = float(input('digite o primeiro termo: '))
l2 = float(input('digite a razão:'))
l3 = 0
while l3 <= 10:
    print('a{} = {}'.format(l3, l1 + l2 * l3))
    l3 = l3 + 1
print('fim!')