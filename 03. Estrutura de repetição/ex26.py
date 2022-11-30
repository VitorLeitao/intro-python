print('Candidatos:\n1 -> BOLSONARO\n2 -> LULA\n3 -> CIRO')
contador_bolsonaro = 0
contador_lula = 0
contador_ciro = 0
num_eleitores = int(input('Digite o numero de eleitores: '))
for c in range(1, num_eleitores + 1):
    voto = int(input('Digite o numero do canditado escolhido(-1 pra alunar): '))
    if voto == 1:
        contador_bolsonaro += 1
    if voto == 2:
        contador_lula += 1
    if voto == 3:
        contador_ciro += 1

if contador_bolsonaro == contador_lula or contador_bolsonaro == contador_ciro or contador_lula == contador_ciro:
    print('Sera necessario um segundo turno.')
else:
    candidatos = ['bolsonaro', 'lula', 'ciro']
    votos = [contador_bolsonaro, contador_lula, contador_ciro]
    maior_numero_votos = max(votos)
    posicao = votos.index(maior_numero_votos)
    ganhador = candidatos[posicao]
    print(f'O ganhador é {ganhador}, com {maior_numero_votos} votos.')


