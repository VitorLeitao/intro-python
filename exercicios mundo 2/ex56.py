l0 = 0
l00 = 0
for c in range(0, 4):
    l1 = input('qual o seu nome')
    l2 = int(input('qual a sua idade'))
    l0 = l0 + l2
    l3 = input('qual o seu genero').strip().lower()
    if l3 == 'masculino':
        if c == 0:
            maior = l2
            nome = l1
        else:
            if l2 > maior:
                maior = l2
                nome = l1
    if l3 == 'feminino':
        if l2 < 20:
            l00 = l00 + 1
print('a media das idades é {}'.format(l0/4))
print('a homem mais velho é {}'.format(nome))
print('o numero de mulheres com menos de 20 é {}'.format(l00))


