l1 = 0
l2 = 0
l3 = 0
while l1 != 999:
    l1 = float(input('digite um numero \ndigite 999 para encerrar'))
    if l1 != 999:
        l2 = l2 + 1
    if l1 != 999:
        l3 = l3 + l1
print('o numero de numeros é: '.format(l2))
print('a media dos numeros é: '.format(l3 / l2))

