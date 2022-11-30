l1 = float(input('digite sua primeira nota'))
l2 = float(input('digite sua segunda nota'))
l3 = (l1 + l2)/2
if l3<5:
    print('reprovado')
elif 5 <= l3 <= 6.7:
    print('recuperação')
else:
    print('aprovado')