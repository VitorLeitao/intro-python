populacao_a = 80000
populacao_b = 200000

while True:
    crescimento_a = input('Digite a taxa de crescimento de A em porcentagem: ')
    try:
        crescimento_a = float(crescimento_a)
        break
    except:
        print('Taca invalida.')

while True:
    crescimento_b = input('Digite a taxa de crescimento de B em porcentagem: ')
    try:
        crescimento_b = float(crescimento_b)
        break
    except:
        print('Taca invalida.')

crescimento_a = crescimento_a / 100
crescimento_b = crescimento_b / 100
contador = 0
while True:
    populacao_a = populacao_a + (populacao_a * crescimento_a)
    populacao_b = populacao_b + (populacao_b * crescimento_b)
    contador += 1
    if populacao_a >= populacao_b:
        break

print(f'Tempo para que as populações se igualem: {contador}')

