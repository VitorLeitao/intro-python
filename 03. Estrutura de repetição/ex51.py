num_n = int(input('Digite um numero inteiro: '))
num_1 = 1
num_2 = 1
total = 0
for c in range(1, num_n + 1):
    if c != num_n:
        print(f'{num_1}/{num_2} + ', end='')
    else:
        print(f'{num_1}/{num_2}')
    num = num_1 / num_2
    total += num
    num_1 += 1
    num_2 += 2

print(f'Soma: {total:.2f}')
