l1 = 1
l2 = int(input('quer ver a tabudada de quem?'))
while True:
    if l2 < 0:
        break
    for c in range(1, 11):
        l3 = l2 * c
        print(f'{l2} x {c} = {l3}')
    l2 = int(input('quer ver a tabuada de quem?'))
print('fim')