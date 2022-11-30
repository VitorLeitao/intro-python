medias = []
for c in range(0, 3):
    print(f'Digite as 5 notas do {c + 1}° aluno.')
    print('=-'*30)
    total = 0
    for i in range(0, 5):
        nota = float(input(f'Digite a {i + 1} nota: '))
        total += nota
    media = total / 5
    medias.append(media)
    print()
medias_boas = []
for c in medias:
    if c >= 7:
        medias_boas.append(c)

print(f'Medias: {medias}')
print(f'Notas aprovadas: {medias_boas}')
