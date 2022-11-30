notas = []
atleta = input('Atleta: ')
for c in range(1, 8):
    nota = float(input(f'{c}° nota: '))
    notas.append(nota)

maximo = max(notas)
minimo = min(notas)
notas.pop(notas.index(maximo))
notas.pop(notas.index(minimo))
media = sum(notas) / len(notas)
print(f'Resultado final:\nAtleta:{atleta}\nMelhor nota:{maximo}\nPior nota: {minimo}\nMedia: {media:.2f}')