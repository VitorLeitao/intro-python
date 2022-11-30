while True:
    letra = input('Digite seu sexo[M/F]: ').upper()
    if letra == 'M':
        print('M - Masculino')
        break
    elif letra == 'F':
        print('F - Feminino')
        break
    else:
        print(f'{letra} - Sexo invalido.')
        continue
