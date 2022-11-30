soma = 0
contador = 0
while True:
    nota = input('Digite a nota(digite algo não numerico para parar a digitção): ')
    if nota.isnumeric():
        nota = float(nota)
        soma += nota
        contador += 1
    else:
        break

media = soma / contador
print(f'A media das notas digitadas é: {media}')
