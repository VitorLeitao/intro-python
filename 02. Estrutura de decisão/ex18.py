data = input('Digite uma data em formato dd/mm/aaaa: ')
if len(data) == 10:
    if data[0:2].isnumeric() and data[3:5].isnumeric() and data[6:]:
        print('Formato VALIDO.')
    else:
        print('Formato INVALIDO.')

else:
    print('Formato INVALIDO.')