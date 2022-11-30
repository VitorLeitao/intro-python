numero = int(input('Digite um numero inteiro de 1-10: '))
print(f'Tabuada de: {numero}')
for c in range(1, 11):
    resultado = numero * c
    print(f'{numero} x {c} = {resultado}')