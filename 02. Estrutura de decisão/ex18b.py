data = input('Digite uma data em formato dd/mm/aaaa: ')

if 5 <= len(data) <= 8:
    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:])
    if 1 <= dia <= 31 and 1 <= mes <= 12:
        print('Formato VALIDO')

    else:
        print('Formato INVALIDO.')

else:
    print('Formato INVALIDO.')