lista_consoantes = []
print('Digite 10 caracteres')
for c in range(1, 11):
    caracter = input(f'Digite o {c}° caracter: ').lower()
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        continue
    else:
        lista_consoantes.append(caracter)

print(f'O usuario digitou {len(lista_consoantes)} consoantes, sendo elas: ', end='')
for c in range(0, len(lista_consoantes)):
    if c == (len(lista_consoantes) - 1):
        print(lista_consoantes[c])
    else:
        print(f'{lista_consoantes[c]} ', end='')