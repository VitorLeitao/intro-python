cardapio = {
    '100': {
        'nome': 'Cachorro Quente',
        'preco': 1.2
    },
    '101': {
        'nome': 'Bauru Simples',
        'preco': 1.3
    },
    '102': {
        'nome': 'Bauru com ovo',
        'preco': 1.5
    },
    '103': {
        'nome': 'Hambúrguer',
        'preco': 1.2
    },
    '104': {
        'nome': 'Cheeseburguer',
        'preco': 1.3
    },
    '105': {
        'nome': 'Refrigerante',
        'preco': 1.0
    }
}

valor_pagar = {'Cachorro Quente': 0, 'Bauru Simples': 0, 'Bauru com ovo': 0, 'Hambúrguer': 0, 'Cheeseburguer': 0, 'Refrigerante': 0}

while True:
    codigo = input('Digite o codigo do produto(-1 pra encerrar): ')
    if codigo == '-1':
        break
    quantidade = int(input('Digite a quantidade desejada: '))
    valor = cardapio[codigo]['preco'] * quantidade
    nome_produto = cardapio[codigo]['nome']
    valor_pagar[nome_produto] = valor

total = 0
for c, i in valor_pagar.items():
    if i > 0:
        total += i
        print(f'{c} : {i}')

print(f'Total: {total}')




