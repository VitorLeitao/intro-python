nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
media = (nota_1 + nota_2) / 2

if 0 <= media < 4:
    conceito = 'E -> REPROVADO'
elif 4 <= media < 6:
    conceito = 'D -> REPROVADO'
elif 6 <= media < 7.5:
    conceito = 'C -> APROVADO'
elif 7.5 <= media < 9:
    conceito = 'B -> APROVADO'
elif 9 <= media <= 10:
    conceito = 'A -> APROVADO'
else:
    conceito = 'INVALIDO'

print(conceito)