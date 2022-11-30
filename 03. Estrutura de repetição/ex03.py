while True:
    nome = input('Digite seu nome: ')
    if len(nome) > 3:
        break
    else:
        print('Digite um nome com mais de 3 caracteres.')
        continue

while True:
    idade = int(input('Digite sua idade: '))
    if 0 <= idade <= 150:
        break
    else:
        print('Digite uma idade válida.')
        continue

while True:
    salario = float(input('Digite seu salario: '))
    if salario >= 0:
        break
    else:
        print('Digite um salario válido.')
        continue

while True:
    sexo = input('Digite seu sexo[M/F]: ').upper()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Digite um sexo valido.')
        continue

while True:
    estado_civil = input('Digite seu estado civil[S, C, V, D]: ').upper()
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        break
    else:
        print('Digite um estado civil valido.')
        continue

print(f'informações:\nnome: {nome}\nidade: {idade}\nsalario: {salario}\nsexo: {sexo}\nestado civil: {estado_civil}')