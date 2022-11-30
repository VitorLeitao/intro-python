quantidade = int(input('Digite um numero inteiro: '))
print(f'numeros primos entre 1 e {quantidade}: ')
for c in range(1, quantidade + 1):
    num = c
    if num == 1:
        continue
    elif (num % 2 == 0 and num != 2) or (num % 3 == 0 and num !=3) or (num % 5 == 0 and num != 5) or (num % 7 == 0 and num != 7):
        continue
    else:
        print(num)