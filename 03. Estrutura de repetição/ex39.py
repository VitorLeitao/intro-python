
for c in range(1, 5):
    info = input('Digite o numero do aluno e sua altura, separada por um espaço: ')
    lista_info = info.split()
    altura = float(lista_info[-1])
    if c == 1:
        maior_altura = altura
        menor_altura = altura
        mais_alto = info
        mais_baixo = info
    else:
        if altura > maior_altura:
            mais_alto = info
            maior_altura = altura
        if altura < menor_altura:
            mais_baixo = info
            menor_altura = altura

print(f'Mais alto: {mais_alto}')
print(f'Mais baixo: {mais_baixo}')

