tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
num = int(input('digite um numero inteiro de 0-10: '))
while num < 0 or num > 10:
    print('numero invalido!')
    num = int(input('digite um numero inteiro de 0-10: '))
print(f'o numero {num} por extenso é {tupla[num]}')