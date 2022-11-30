contador = 1
soma = 0
while True:
    produto = float(input(f'Produto {contador}: '))
    if produto == 0:
        break
    contador += 1
    soma += produto

print(f'Total: {soma}')
dinheiro = float(input('Dinheiro cliente: '))
troco = dinheiro - soma
print(f'Troco: {troco}')