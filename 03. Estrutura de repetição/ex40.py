codigos = []
veiculos = []
acidentes = []
acidentes_menos_2000 = []
for c in range(0, 5):
    codigo = input('Digite o codigo da cidade: ')
    num_veiculos = int(input(f'Digite o numero de veiculos na cidade {codigo}: '))
    num_acidentes = int(input(f'Digite o numero de acidentes na cidade {codigo}: '))
    codigos.append(codigo)
    veiculos.append(num_veiculos)
    acidentes.append(num_acidentes)
    if num_veiculos < 2000:
        acidentes_menos_2000.append(num_acidentes)
    print()


media_veiculos = sum(veiculos) / 5
mais_acidentes = max(acidentes)
menos_acidentes = min(acidentes)
cidade_mais_acidentes = codigos[acidentes.index(mais_acidentes)]
cidade_menos_acidentes = codigos[acidentes.index(menos_acidentes)]
media_acidentes_2000 = sum(acidentes_menos_2000) / len(acidentes_menos_2000)

print(f'Maior indice de acidentes: {mais_acidentes}(cidade: {cidade_mais_acidentes})')
print(f'Menor indice de acidentes: {menos_acidentes}(cidade: {cidade_menos_acidentes})')
print(f'Media de veiculos nas 5 cidades: {media_veiculos}')
print(f'Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {media_acidentes_2000}')
