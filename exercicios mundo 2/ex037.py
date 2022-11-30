l1 = int(input('digite um numero'))
print('para binario = 1'"\n"'para octal = 2'"\n"'para hexadecimal = 3')
l2 = input('voce quer convertar pra qual?')
if l2 == '1':
    print('o numero {} em codigo binario é {}'.format(l1, bin(l1)))
elif l2 == '2':
    print('o numero {} em octal é {}'.format(l1, oct(l1)))
else:
    print('o numero {} em hexadecimal é {}'.format(l1, hex(l1)))