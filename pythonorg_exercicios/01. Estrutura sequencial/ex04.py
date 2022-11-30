soma = 0
contador = 0
while contador < 4:
    contador += 1
    nota = float(input(f'digite a {contador}° nota do bimeste: '))
    soma += nota


media = soma / contador
print(f'a media do bimestre é: {media}')