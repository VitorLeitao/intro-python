lista = []
print('Digite 5 numeros')
print('=-'*30)
for c in range(0, 5):
    num = float(input('Digite um numero: '))
    lista.append(num)

print()
print('Lista em ordem inversa:')
for c in range(len(lista) - 1, -1, -1):
    print(lista[c])