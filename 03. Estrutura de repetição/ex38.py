salario = float(input('Digite o salario inicial: '))
ano_atual = int(input('Digite o ano atual: '))
aumento = 1.5
for c in range(1996, ano_atual + 1):
    salario = salario + (salario * (aumento / 100))
    aumento = aumento * 2

print(f'O salario atual é: {salario:.2f}')