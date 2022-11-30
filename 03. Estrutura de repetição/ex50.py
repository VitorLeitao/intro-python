num_h = int(input('Digite um numero inteiro: '))
total = 0
for c in range(1, num_h + 1):
    num = 1 / c
    total += num

print(f'Soma = {total:.2f}')


