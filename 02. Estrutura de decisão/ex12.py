qt_horas = int(input('Digite a quantidade de horas trabalhadas em um mes: '))
valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
salario_bruto = qt_horas * valor_hora
inss = 0.1
fgts = 0.11

if salario_bruto <= 900:
    imposto_renda = 0
elif 900 < salario_bruto <= 1500:
    imposto_renda = 0.05
elif 1500 < salario_bruto <= 2500:
    imposto_renda = 0.1
else:
    imposto_renda = 0.2

valor_inss = inss * salario_bruto
valor_fgts = fgts * salario_bruto
valor_ir = imposto_renda * salario_bruto
total_descontos = valor_inss +  valor_ir
salario_liquido = salario_bruto - total_descontos

print(f'Salario bruto: R${salario_bruto}')
print(f'(-) IR ({imposto_renda * 100}%): R${valor_ir}')
print(f'(-) INSS ({inss * 100}%): R${valor_inss}')
print(f'FGTS ({fgts * 100}%): R${valor_fgts}')
print(f'Total de descontos: R${total_descontos}')
print(f'Salario liquido: R${salario_liquido}')


