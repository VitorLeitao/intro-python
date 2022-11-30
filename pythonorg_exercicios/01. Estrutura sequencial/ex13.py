altura = float(input('digite sua altura: '))
if altura > 5:
    altura = altura / 100
while True:
    sex = input('digite seu sexo[M/F]: ').upper()
    if sex == 'M' or sex == 'F':
        break
    print('esse sexo nao existe')

if sex == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f'com uma altura de {altura}cm, seu peso ideal seria: {peso_ideal}')
