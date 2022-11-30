lista = []
for c in range(0, 5):
    num = float(input('Digite um numero: '))
    lista.append(num)

lista_quadrado = []
for c in lista:
    num = c ** 2
    lista_quadrado.append(num)

soma = sum(lista_quadrado)
print(f'A soma do quadrado dos numeros é: {soma}')