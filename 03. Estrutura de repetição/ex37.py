pesos = []
alturas = []
codigos = []
soma_peso = 0
soma_altura = 0
contador = 0
while True:
    codigo = input('Digite o seu codigo(0 pra encerrar): ')
    if codigo == '0':
        break
    peso = float(input('Digite seu peso em Kg: '))
    altura = float(input('Digite sua altura em M: '))
    pesos.append(peso)
    alturas.append(altura)
    codigos.append(codigo)
    soma_peso += peso
    soma_altura += altura
    contador += 1

maior_peso = max(pesos)
mais_pesado = codigos[pesos.index(maior_peso)]
menor_peso = min(pesos)
menos_pesado = codigos[pesos.index(menor_peso)]
media_peso = sum(pesos) / contador


maior_altura = max(alturas)
mais_alto = codigos[alturas.index(maior_altura)]
menor_altura = min(alturas)
menos_alto = codigos[alturas.index(menor_altura)]
media_altura = sum(alturas) / contador

print(f'O aluno mais alto é o {mais_alto} com {maior_altura}M.')
print(f'O aluno mais baixo é o {menos_alto} com {menor_altura}M')
print(f'A media das alturas dentre os alunos da academia é: {media_altura:.2f}M')
print()
print(f'O aluno mais pesado é o {mais_pesado} com {maior_peso}Kg')
print(f'O aluno mais leve é o {menos_pesado} com {menor_peso}Kg')
print(f'A media do peso dentre os alunos da academia é: {media_peso:.2f}Kg')




