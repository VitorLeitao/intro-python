lista = []
while True:
    lista.append(int(input('digite um numero inteiro: ')))
    hm = input('voce deseja cntinuar[S/N]? ').strip().lower()
    if hm == 'n':
        break

print(f'A)foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'B) a lista em ordem decrescente é {lista}')
if 5 in lista:
    print('C) o numero 5 está dentro da lista!')
else:
    print('C) o numero 5 não esta dentro da lista')