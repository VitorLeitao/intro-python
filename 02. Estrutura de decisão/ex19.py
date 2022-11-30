numero = int(input('Digite um numero menor que 1000: '))
if numero < 1000:
    centenas = numero // 100
    numero = numero - (100 * centenas)
    dezenas = numero // 10
    numero = numero - (dezenas * 10)
    unidades = numero
    lista = [centenas, 'centena', dezenas, 'dezena', unidades, 'unidade']
    lista_certa = []
    for c in range(0, 6, 2):
        if lista[c] != 0:
            lista_certa.append(lista[c])
            if lista[c] > 1:
                lista_certa.append(f'{lista[c + 1]}s')
            else:
                lista_certa.append(lista[c + 1])

    if len(lista_certa) == 6:
        print(f'{lista_certa[0]} {lista_certa[1]}, {lista_certa[2]} {lista_certa[3]} e {lista_certa[4]} {lista_certa[5]}')
    elif len(lista_certa) == 4:
        print(f'{lista_certa[0]} {lista_certa[1]} e {lista_certa[2]} {lista_certa[3]}')
    elif len(lista_certa) == 2:
        print(f'{lista_certa[0]} {lista_certa[1]}')
    else:
        print('O numero nao tem esses bagui')
else:
    print('Numero invalido')