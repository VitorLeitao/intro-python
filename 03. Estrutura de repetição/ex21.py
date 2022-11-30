while True:
    num = int(input('Digite um numero inteiro: '))
    if num == 0 or num == 1:
        print('O numero NÃO é primo.')
    else:
        if (num % 2 == 0 and num != 2) or (num % 3 == 0 and num != 3) or (num % 5 == 0 and num != 5) or (num % 7 == 0 and num != 7):
            print('O numero NÃO é primo, ele é divisivel por: .')
        else:
            print('O numero é primo.')
    intencao = input('\nDeseja continuar a digitar[S/N]? ').upper()
    if not intencao == 'S':
        break
