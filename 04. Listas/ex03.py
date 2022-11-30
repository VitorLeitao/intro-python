notas = []
print('Digite as 4 notas do aluno.')
print('=-'*30)

for c in range(1, 5):
    nota = float(input(f'Digite a {c}° nota: '))
    notas.append(nota)

print('Notas: ', end='')
for c in notas:
    if c == (len(notas)- 1):
        print(c)
    else:
        print(f'{c}, ', end='')

media = sum(notas) / len(notas)
print(f'Media: {media}')
