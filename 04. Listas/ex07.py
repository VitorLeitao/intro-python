lista = []
mult = 1
for c in range(0, 5):
    num = float(input(f'Digite o {c + 1} numero: '))
    mult = mult * num
    lista.append(num)

soma = sum(lista)
print(f'Vetor: {lista}')
print(f'Soma: {soma}')
print(f'Multiplicação: {mult}')
