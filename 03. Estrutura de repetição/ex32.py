num = int(input('Digite um numero inteiro: '))
print(f'Fatorial de {num}')
contador = num
resultado = 1
print(f'{num}! = ', end='')
while True:
    print(contador, end='')
    resultado = resultado * contador
    contador -= 1
    if contador <= 1:
        break
    print(' . ', end='')
print(f' = {resultado}')