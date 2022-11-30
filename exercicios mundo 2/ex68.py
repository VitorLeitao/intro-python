import random

print('vamosjogar par ou impar')
l1 = 0
l4 = int(input('escolha um numero de um a dez'))
l5 = input('voce quer par ou impar?').strip().lower()
while True:
    l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l3 = random.choice(l2)
    l6 = l3 + l4
    if l6 % 2 == 0:
        ngc = 'par'
    else:
        ngc = 'impar'
    print(f'voce jogou {l4} e o computador {l3}, a soma foi {l6}, ou seja {ngc}')
    if l5 != ngc:
        print('perdeu!')
        break
    l1 = l1 + 1
    print('ganhou!!')
    l5 = input('voce quer ser par ou impar no segundo game? ').strip().lower()
    l4 = int(input('digite outroi numero de 1 a dez'))
print(f'fim, voce venceu {l1} vezes')


