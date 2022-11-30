l1 = 0
for c in range(0, 7):
    l2 = int(input('digite o ano de nascimento'))
    l3 = 2021 - l2
    if l3 >= 18:
        l1 = l1 + 1
print('o numero de pessoas maiores de idade e: {}'.format(l1))