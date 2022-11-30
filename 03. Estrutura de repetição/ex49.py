num_1 = 1
num_2 = 1
num_n = int(input('Digite um numero inteiro: '))
while True:
    print(f'{num_1}/{num_2}')
    num_1 += 1
    num_2 += 2
    if num_1 > num_n:
        break