contador_1 = contador_2 = contador_3 = contador_4 = 0
while True:
    num = float(input('Digite um numero inteiro entre 1 - 100(-1 pra encerrar): '))
    if num == -1:
        break
    if 0 <= num <= 25:
        contador_1 += 1
    if 26 <= num <= 50:
        contador_2 += 1
    if 51 <= num <= 75:
        contador_3 += 1
    if 76 <= num <= 100:
        contador_4 += 1
    print()

print(f'Existem {contador_1} numeros dentre os digitados no intervalo de: [0-25]')
print(f'Existem {contador_2} numeros dentre os digitados no intervalo de: [26-50]')
print(f'Existem {contador_3} numeros dentre os digitados no intervalo de: [51-75]')
print(f'Existem {contador_4} numeros dentre os digitados no intervalo de: [76-100]')