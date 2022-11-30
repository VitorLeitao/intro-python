numero_turmas = int(input('Digite o numero de turmas: '))
soma = 0
for c in range(0, numero_turmas):
    while True:
        num = int(input(f'Digite o numero de alunos na turma {c + 1}: '))
        if num <= 40:
            soma += num
            break
        else:
            print('A turma nao pode ter mais de 40 alunos.')

media = soma / numero_turmas
print(f'A media de alunos por turma é: {media}')