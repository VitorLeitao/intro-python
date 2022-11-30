l1 = float(input('qual o preço do produto?'))
print('a vista no dinheiro = 1' '\n''a vista no cartão = 2'"\n"'em ate 2x no cartão = 3'"\n"'em ate 3x no cartão = 4')
l2 = input('qual a condição de pagamento?')
if l2 == '1':
    l3 = l1*0.9
    print('o novo preço sera {}'.format(l3))
elif l2 == '2':
    l3 = l1*0.95
    print('o novo preço sera {}'.format(l3))
elif l2 == '3':
    print('o preço sera o mesmo do inicial, {}'.format(l1))
else:
    l3 = l1*1.2
    print('o novo preço sera de {}'.format(l3))



