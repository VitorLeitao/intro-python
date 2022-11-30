l1 = 0
for c in range(0, 6):
    l2 = int(input('digite um numero'))
    if l2 % 2 == 0:
        l1 = l1 + l2
print('a soma dos pares é {}'.format(l1))