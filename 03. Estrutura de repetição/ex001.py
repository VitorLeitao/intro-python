while True:
    nota = input('Digite uma nota de 0-10: ')
    try:
        nota = float(nota)
        break
    except:
        print('ERROR, digite mais uma vez.')
        continue
