l1 = int(input('digite o ano de seu nascimento'))
l2 = 2021 - l1
if l2 == 18:
    print('esta no ano de se alistar')
elif l2<18:
    print('ainda não é o ano')
else:
    print('ja passou do ano')