salario = float(input('Digite seu salário: '))
if salario <= 280:
    aumento = 0.2
elif 280 < salario <= 700:
    aumento = 0.15
elif 700 < salario <= 1500:
    aumento = 0.1
elif salario > 1500:
    aumento = 0.05
else:
    aumento = 0

valor_aumento = aumento * salario
novo_salario = salario + valor_aumento
print(f'Salario antido: {salario}.')
print(f'Percentual do aumento: {aumento}.')
print(f'Valor do aumento: {valor_aumento}.')
print(f'Novo salario: {novo_salario}.')
