# Variaveis das porcentagens a se pagar
imposto_renda = 0.11
inss = 0.08
sindicato = 0.05

dinheiro = float(input('digite o valor da sua hora de trabalho: '))
horas = int(input('digite a quantidade de horas trabalhadas em um mes: '))
salario_bruto = dinheiro * horas

# Valores pagos
valor_imposto = salario_bruto * imposto_renda
valor_inss = salario_bruto * inss
valor_sindicato = salario_bruto * sindicato
total_descontos = valor_imposto + valor_inss + valor_sindicato

salario_liquido = salario_bruto - total_descontos
print(f'+ Salario bruto : R${salario_bruto}')
print(f'- IR(11%) : R${valor_imposto}')
print(f'- INSS(8%) : R${valor_inss}')
print(f'- Sindicato(5%) : R${valor_sindicato}')
print(f'= Salario liquido : R${salario_liquido}')