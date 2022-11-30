saltos = []
while True:
    nome = input('Digite o nome do atleta(nada pra encerrar): ')
    if len(nome) == 0:
        break
    for c in range(0, 5):
        salto = float(input(f'{c + 1}° salto: '))
        saltos.append(salto)
    maximo = max(saltos)
    minimo = min(saltos)
    saltos.pop(saltos.index(maximo))
    saltos.pop(saltos.index(minimo))
    media = sum(saltos) / 3
    print(f'Melhor salto: {maximo}')
    print(f'Pior salto: {minimo}')
    print(f'Media dos demais: {media:.2f}')
    print()
    print(f'Resultado final:\n{nome}: {media:.2f}m')
