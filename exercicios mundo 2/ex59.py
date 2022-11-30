print('operações com numero pre-definidos')
l1 = float(input('digite o primeiro numero: '))
l2 = float(input('digite o segundo numero: '))
print('\n [1] = somar' '\n [2] = multiplicar' '\n [3] = maior/menor' '\n [4] = novos numeros' '\n [5] = finalizar programa')
l3 = input('o ue deseja fazer com os numeros? ')
while l3 != '5':
    if l3 == '1':
        print('{} + {} = {}'.format(l1, l2, l1 + l2))
    if l3 == '2':
        print('{} x {} = {}'.format(l1, l2, l1 * l2))
    if l3 == '3':
        if l1 > l2:
            print('{} > {}'.format(l1, l2))
        else:
            print('{} > {}'.format(l2, l1))
    if l3 == '4':
        l1 = float(input('qual sera o novo primeiro numero? '))
        l2 = float(input('qual sera o novo segundo numero? '))
    l3 = input('o que deseja fazer agora?')
print('programa finalizado!')