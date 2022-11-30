num = int(input('Digite um numero inteiro: '))
const = num
resultado = 1
print(f'{num}! = ', end='')
for c in range(0, const):

    if c == (const - 1):
        print(num, end='')
    else:
        print(f'{num}.',end='')
    resultado = resultado * num
    num -= 1

print(f' = {resultado}')
