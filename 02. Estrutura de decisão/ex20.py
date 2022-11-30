notas = []
for c in range(0, 3):
    nota = float(input(f'Digite a {c + 1}° nota: '))
    notas.append(nota)

soma = sum(notas)
media = soma / 3
if media >= 7:
    if media == 10:
        print('Aprovado com distinção')
    else:
        print('Aprovado')
elif 0 < media < 7:
    print('Reprovado')
else:
    print('Erro na digitação.')