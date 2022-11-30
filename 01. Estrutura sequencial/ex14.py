peso = float(input('digite o peso do peixe(Kg): '))
limite = 50
excesso = peso - limite

if excesso < 0:
    excesso = 0

multa = excesso * 4
print(f'A multa que devera ser paga por passar do limite de {limite}Kg em {excesso}Kg é: {multa}')