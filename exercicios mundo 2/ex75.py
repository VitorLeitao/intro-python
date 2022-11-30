num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
num3 = int(input('digite o terceiro numero: '))
num4 = int(input('digite o quarto numero: '))

tupla = (num1, num2, num3, num4)

print(f'a tupla foi {tupla}')

#alternativa A
numero_vezes = tupla.count(9)
print(f'A) o numero 9 apareceu {numero_vezes} vezes')

#alternativa B
posicao = int(tupla.index(3))
print(f'B) a posição que foi digitada o primeiro numero 3 foi {posicao + 1}°')

#alternativa C
print('C) os numeros pares foram: ', end = '')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print(tupla[c], ', ', end = '')
