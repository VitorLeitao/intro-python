soma = 0
contador = 1
while True:
    temp = input(f'Digite a {contador} temperatura(caracter pra parar a leitura): ')
    if not temp.isnumeric():
        break
    temp = float(temp)
    soma += temp
    if contador == 1:
        max = temp
        min = temp
    else:
        if temp > max:
            max = temp
        if temp < min:
            min = temp
    contador += 1
if contador > 1:
    media = soma / (contador - 1)
else:
    media = 0
print(f'Maior temperatura: {max}')
print(f'Menor temperatura: {min}')
print(f'Media das temperaturas: {media}')