import random
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
for c in range(0, 5):
    if c ==0:
        maior = tupla[c]
        menor = tupla[c]
    else:
        if tupla[c] > maior:
            maior = tupla[c]
        if tupla[c] < menor:
            menor = tupla[c]
print(f'os numeros sorteados foram {tupla}')
print(f'o amior numero da tupla é {maior} e o menor {menor}')