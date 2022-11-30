base = int(input('Digite a base(inteiro): '))
expoente = int(input('Digite o expoente(inteiro): '))
resultado = 1
for c in range(0, expoente):
    resultado = resultado * base

print(f'O resultado é: {resultado}')