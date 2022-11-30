contador = 0
print('Responda as perguntas apenas com [S/N]')
pergunta_1 = input('Telefonou para a vítima? ').upper()
if pergunta_1 == 'S':
    contador += 1
pergunta_2 = input('Esteve no local do crime? ').upper()
if pergunta_2 == 'S':
    contador += 1
pergunta_3 = input('Mora perto da vítima? ').upper()
if pergunta_3 == 'S':
    contador += 1
pergunta_4 = input('Devia para a vítima? ').upper()
if pergunta_4 == 'S':
    contador += 1
pergunta_5 = input('Já trabalhou com a vítima? ').upper()
if pergunta_5 == 'S':
    contador += 1

if contador == 5:
    print('Voce foi julgado como ASSASSINO.')
elif 3 <= contador <= 4:
    print('Voce foi julgado como CUMPLICE.')
elif contador == 2:
    print('Voce foi julgado como SUSPEITO')
else:
    print('Voce foi julgado como INOCENTE')
