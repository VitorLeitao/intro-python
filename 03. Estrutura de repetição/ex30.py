preco_pao = float(input('Preço do pão: '))
print('Panificadora Pão de Ontem - Tabela de preços')
for c in range(1, 51):
    valor = preco_pao * c
    print(f'{c} - R${valor:.2f}')