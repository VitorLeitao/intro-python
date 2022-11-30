l1 = l2 = l3 = 0
while True:
    print('vamos cadastrar uma pessoa')
    idade = int(input('qual a idade da pessoa'))
    sexo = input('digite seu genero [F/M]').strip().lower()
    while sexo != 'm' and sexo != 'f':
        sexo = input('sexo invalido, digite novamente: ')
    if idade > 18:
        l1 = l1 + 1
    if sexo == 'm':
        l2 = l2 + 1
    if sexo == 'f':
        if idade < 20:
            l3 = l3 + 1
    l5 = input('voce quer continuar?(S/N)').strip().lower()
    if l5 == 'n':
        break
print(f'o numero de pessoas com +18 é {l1}, o numero de homens é {l2}, e o num3ero de mulheres menores que 20 é {l3}')
