l1 = float(input('digite o primeiro numero'))
l2 = float(input('digite o segundo numero'))
if l1>l2:
    print('o primeiro é maior que o segundo, que sao respectivamente {:.2f} e {:.2f}'.format(l1, l2))
elif l2>l1:
    print('o segundo é maior que o primeiro, sendo eles {:.2f} e {:.2f}, respectivamente'.format(l2, l1))
else:
    print('os dois são iguais')