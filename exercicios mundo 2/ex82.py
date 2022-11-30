lista_a = []
lista_b = []
lista_c = []
while True:
    termo = int(input('digite um numero inteiro: '))
    lista_a.append(termo)
    if termo % 2 == 0:
        lista_b.append(termo)
    else:
        lista_c.append(termo)
    continuar = input('deseja continuar digitando[S/N]? ').strip().lower()
    if continuar == 'n':
        break

lista_a.sort()
lista_b.sort()
lista_c.sort()
print('='*100)
print(f'a lista dos numeros digitados foi: {lista_a}, a dos pares: {lista_b} e dos impares: {lista_c}')
