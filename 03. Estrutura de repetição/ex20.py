while True:
    num = input('Digite um numero inteiro menor que 16: ')
    if num.isnumeric():
        num = int(num)
        if num == 1 or num == 0:
            print(f'{num}! = 1')
        elif num < 16 and num != 0 and num != 1:
            const = num
            resultado = 1
            print(f'{num}! = ', end='')
            for c in range(0, num):
                if c == (const - 1):
                    print(num, end='')
                else:
                    print(f'{num}.', end='')
                resultado = resultado * num
                num = num - 1
            print(f' = {resultado}')
        else:
            print('ERROR')
            continue

    else:
        print('ERROR')
        continue
    intencao = input('Deseja continuar digitando[S/N]? ').upper()
    if intencao != 'S':
        break
