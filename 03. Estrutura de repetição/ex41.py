lista_porcentagem = [10, 15, 20, 25]
divida = float(input('Digite o valor da sua divida: '))
contador = 0
print(f'Valor da divida -> {divida}\nValor dos juros -> 0.0\nQuantidade de parcelas -> 1\nValor da parcela -> {divida}')
print()
for c in range(3, 13, 3):
    juros = (divida * (lista_porcentagem[contador] / 100))
    nova_divida = divida + juros
    valor_parcela = nova_divida / c
    contador += 1
    print(f'Valor da divida -> {nova_divida:.2f}\nValor dos juros -> {juros:.2f}\nQuantidade de parcelas -> {c}\nValor da parcela -> {valor_parcela:.2f}')
    print()