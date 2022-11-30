lista = []
while True:
    num = int(input('digite um numero inteiro, se ele ja estiver na lista, sera apagado: '))
    if num in lista:
        print('numero anulado!!')
    else:
        lista.append(num)
    cont = input('voce deseja continuar [S/N] ?').strip().lower()
    if cont == 'n':
        break
print(f'os numeros em ordem crescente são: {sorted(lista)}')