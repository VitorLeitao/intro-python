lista = ['Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']

num = input('Digite um numero de 1-7: ')
if num.isnumeric():
    num = int(num)
    if 1 <= num <= 7:
        num = num -1
        dia = lista[num]
    else:
        dia = 'inválido'
else:
    dia = 'inválido'

print(f'O dia correspondente ao numero digitado é: {dia}')

