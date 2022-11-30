import random

print('o jogo consiste em acertar o numero que o computador escolherá')
l0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = random.choice(l0)
l2 = 1
l3 = int(input('digite um numero de 0 - 10: '))
while l3 != l1:
    l3 = int(input('digite novamente: '))
    l2 = l2 + 1
print('voce acertou o numero em {} tentativas'.format(l2))