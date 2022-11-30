entrada = input('Digite numeros quaisquer: ').split()
lista = []
soma = 0
for c in entrada:
    c = int(c)
    soma += c
    lista.append(c)

print(f'O menor valor da lista fornecida é: {min(lista)}')
print(f'O maior valor da lista fornecida é: {max(lista)}')
print(f'A soma dos valores da lista é: {soma}')
