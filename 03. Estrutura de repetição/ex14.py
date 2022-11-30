impar = 0
par = 0
for c in range(0, 5):
    num = float(input('Digite um numero: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Quantidade de numeros pares: {par}')
print(f'Quantidade de numeros impares: {impar}')