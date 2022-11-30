soma = 0
contador = 0
while True:
    idade = float(input(f'Digite a idade da {contador + 1}° pessoa. -1 para parar a contagem: '))
    if idade == -1:
        break
    else:
        soma += idade
        contador += 1

media = soma / contador
turma = ''
if 0 <= media <= 25:
    turma = 'Jovem'
elif 25 < media <= 60:
    turma = 'Adulta'
elif media > 60:
    turma = 'Idosa'

print(f'A turma é {turma}')

