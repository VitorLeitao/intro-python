l0 = 0
l1 = int(input('digite um numero'))
for c in range(1, l1+1):
    if l1 % c == 0:
        l0 = l0 + 1
    else:
        l0 = l0
if l0 == 2:
    print('o numero é primo!')
else:
    print('o numero não é primo!')