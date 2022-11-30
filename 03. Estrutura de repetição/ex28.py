num_cd = int(input('Digite o numero de CDs na sua coleção: '))
valor_total = 0
for c in range(0, num_cd):
    valor = float(input(f'Digite o valor do {c + 1} CD: '))
    valor_total += valor

print(f'O valor total investido foi: {valor_total}')