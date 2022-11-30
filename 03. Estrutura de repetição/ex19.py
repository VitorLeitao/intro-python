lista = []
while True:
    num = int(input('Digite um numero inteiro menor que 1000: '))
    if num >= 1000:
        print('Numero INVALIDO.')
        continue
    else:
        lista.append(num)
        intencao = input('Deseja continuar digitando[S/N]? ').upper()
        if intencao == 'N':
            break

soma = sum(lista)
maximo = max(lista)
minimo = min(lista)
print(f'A soma dos numeros digitados é: {soma}')
print(f'O menor numero digitado foi: {minimo}')
print(f'O maior numero digitado foi: {maximo}')