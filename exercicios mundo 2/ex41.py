l0 = input('qual o seu nome?')
l1 = int(input('digite seu ano de nascimento'))
l2 = 2021 - l1
if l1 <= 9:
    print('{} é da categoria mirim'.format(l0))
elif 9 < l2 <= 14:
    print('{} é da categoria infantil'.format(l0))
elif 14 < l2 <= 19:
    print('{} é da categoria junior'.format(l0))
elif 19 < l2 <= 20:
    print('{} é da categoria senior'.format(l0))
else:
    print('{} é da categoria master'.format(l0))