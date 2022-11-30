lista_1 = []
lista_2 = []
lista_intercalada = []
for c in range(1, 3):
    print(f'Digite os elementos da {c}° lista.')
    print('=-'*30)
    for i in range(1, 4):
        num = input(f'Digite o {i}° elemento da {c}° lista: ')
        if c == 1:
            lista_1.append(num)
        else:
            lista_2.append(num)

for c in range(0, 3):
    lista_intercalada.append(lista_1[c])
    lista_intercalada.append(lista_2[c])

print(f'Lista intercalada:\n{lista_intercalada}')