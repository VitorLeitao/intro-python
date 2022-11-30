while True:
    turno = input('Digite seu tuno[M/V/N]: ').upper()
    if turno == 'M':
        print('Bom dia!')
        break
    if turno == 'V':
        print('Boa tarde!')
        break
    if turno == 'N':
        print('Boa noite!')
        break
    else:
        print('turno invalido')
        continue
