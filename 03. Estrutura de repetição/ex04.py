populacao_a = 80000
crescimento_a = 1.03
populacao_b = 200000
crescimento_b = 1.015
contador = 0

while True:
    populacao_a = populacao_a * crescimento_a
    populacao_b = populacao_b * crescimento_b
    contador += 1
    if populacao_a >= populacao_b:
        break


print(f'Tempo para que as populações se igualem: {contador}')