numeros = input('digite dois numeros inteiros separados por um space: ')
if len(numeros) == 3:
    if numeros[0].isnumeric() and numeros[2].isnumeric():
        num1 = int(numeros[0])
        num2 = int(numeros[2])
        soma = num1 + num2
        frase = f'a soma dos numeros digitados é: {soma}'
    else:
        frase = 'erro na digitação'
else:
    frase = 'erro na digitação'
print(frase)