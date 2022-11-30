l1 = l2 = l3 = l4 = l5 = l6 = 0
while True:
    din = int(input('digite aquantidade de dinheiro a ser tirada: '))
    l1 = din // 100
    din = din - 100 * l1

    l2 = din // 50
    din = din - l2 * 50

    l3 = din // 20
    din = din - l3 * 20

    l4 = din // 10
    din = din - l4 * 10

    l5 = din // 5
    din = din - l5 * 5

    l6 = din // 2
    din = din - l6 * 2

    print(f'o numero de notas de 100 = {l1}\no nuemro de notas de 50 = {l2}\no numero de notas de 20 = {l3}\no numero de notas de 10 = {l4}\no numero de notas de 5 = {l5}\no numero de notas dde 2 = {l6}')
    cod = input('deseja continuar?[s/n]: ')
    if cod == 'n':
        break
print('fim')





