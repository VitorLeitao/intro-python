l1 = l2 = l3 = 0
while True:
    nome = input('digite o nome do produto')
    preço = float(input('digite o preço do produto'))
    l1 = l1 + preço
    if preço > 1000:
        l2 = l2 + 1
    if l3 == 0:
        menor = nome
        menorvalor = preço
    else:
        if preço < menorvalor:
            menor = nome
            menorvalor = preço
    l3 = l3 + 1
    l4 = input('voce deseja continuar? [S/N]').strip().lower()
    if l4 == 'n':
        break
print(f'o total é {l1}, o numero de produtos mais caros quew 1000 é {l2} e o nome do produto mais bataro é {menor}')