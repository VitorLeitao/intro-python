import random

print('mini game jokeno')
l1 = input('escolha entre pedra, papel ou tesoura').strip().lower()
l2 = random.choice(['pedra', 'papel', 'tesoura'])
if l1 == 'pedra':
    if l2 == 'pedra':
        print('o computador escolheu: PEDRA''\n''empate!')
    elif l2 == 'tesoura':
        print('o computador escolheu PEDRA''\n''vitoria!')
    else:
        print('o computador escolheu PAPEL''\n''derrota!')
elif l1 == 'papel':
    if l2 == 'papel':
        print('o computador escolheu PAPEL''\n''empate!')
    elif l2 == 'pedra':
        print('o computador escolheu PEDRA''\n''vitoria!')
    else:
        print('o computador escolheu tesoura''\n''derrota!')
else:
    if l2 == 'tesoura':
        print('o computador escolheu tesoura''\n''empate!')
    elif l2 == 'papel':
        print('o computador escolheu papel''\n''vitoria!')
    else:
        print('o computador escolheu pedra''\n''derrota!')
