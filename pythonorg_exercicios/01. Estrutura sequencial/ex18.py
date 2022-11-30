tamanho_arquivo = float(input('Digite o tamnho do arquivo(MB): '))
velocidade_net = float(input('Digite a velocidade da internet(Mbps): '))
tempo_segundos = tamanho_arquivo / velocidade_net
tempo_minutos = tempo_segundos / 60
print(f'Vai levar {tempo_minutos:.2} minutos pra baixar o arquivo.')