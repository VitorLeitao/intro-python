lista = []
for c in range(0, 5):
    num = float(input('Digite um numero: '))
    lista.append(num)

maximo = max(lista)
print(f'O maior valor dentre os digitados é: {maximo}')