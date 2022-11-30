altura = float(input('digite sua altura: '))
if altura > 5:
    altura = altura / 100
peso_ideal = (72.7 * altura) - 58
print(f'com uma altura de {altura}m, o seu peso ideal é {peso_ideal}kg')