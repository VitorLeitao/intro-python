while True:
    num = input('Digite um numero inteiro(caracter pra encerrar): ')
    if not num.isnumeric():
        break
    num = int(num)
    if num == 0 or num == 1:
        print(f'{num} NÃO é primo.')
    elif (num % 2 == 0 and num != 2) or (num % 3 == 0 and num !=3) or (num % 5 == 0 and num != 5) or (num % 7 == 0 and num != 7):
        print(f'{num} NÃO é primo.')
    else:
        print(f'{num} é primo.')