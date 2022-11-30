print('vamos calcular uma PA!!!')
l1 = float(input('digite o primeiro termo: '))
l2 = float(input('digite o segundo termo: '))
l3 = 0
while l3 <= 10:
    print('a{} = {}'.format(l3, l1 + l2 * l3))
    l3 = l3 + 1
l4 = int(input('quantos numeros da sequencia voce quer ver a mais? \ncaso nao queria, digite 0'))
if l4 != 0:
    while (l3 - 10) <= l4:
        print('a{} = {}'.format(l3, l1 + l2 * l3 ))
        l3 = l3 + 1
    print('fim!')
else:
    print('fim!')
