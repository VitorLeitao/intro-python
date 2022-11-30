num = input('Digite um numero inteiro: ')
lista = list(num)
num_2 = ''

for c in range(len(num) - 1, -1, -1):
    num_2 += lista[c]

print(f'=> {num_2}')