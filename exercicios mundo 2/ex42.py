
l1 = float(input('digite o primero lado'))
l2 = float(input('digite o segundo lado'))
l3 = float(input('digite o terceiro lado'))
if l1 < l2 + l3 or l2 < l1 + l3 or l3 < l1 + l2:
    print('pode formar um triangulo!', end='')
    if l1 == l2 == l3:
        print('e é um triangulo equilatero')
    elif l1 != l2 != l3:
        print('e é um triangulo escaleno')
    else:
        print('e é um triangulo isosceles')
else:
    print('não pode formar um triangulo!')