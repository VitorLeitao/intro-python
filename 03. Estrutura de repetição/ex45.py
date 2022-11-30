gabarito = {
    '1': '',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': '',
    '10': '',
}
notas = []
for c in range(1, 11):
    resposta_professor = input(f'Digite a resposta da {c}° questão: ').lower()
    gabarito[c] = resposta_professor
print()

contador = 0
while True:
    contador += 1
    total = 0
    for c in range(1, 11):
        resposta_aluno = input(f'Digite a resposta do aluno para a {c}° questão: ').lower()
        if resposta_aluno == gabarito[c]:
            total += 1
        print()
    notas.append(total)
    confirmacao = input('Deseja continuar digitando[S/N]? ').lower()
    if confirmacao == 'n':
        break

soma = sum(notas)
media = soma / contador
print(f'A maior quantidade de acertos foi: {max(notas)}')
print(f'A menor quantidade de acertos foi: {min(notas)}')
print(f'O numero de alunos que ultilizaram o sistema foi: {contador}')
print(f'A media das notas foi: {media:.2f}')
