num_1 = int(input('Digite um numero inteiro: '))
num_2 = int(input('Digite outro numero inteiro: '))
soma = 0
for c in range(num_1 + 1, num_2):
    print(c)
    soma += c
print(f'A soma dos numeros é: {soma}')