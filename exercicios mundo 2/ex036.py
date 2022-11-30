l1 = float(input('digite o valor da casa'))
l2 = float(input('em quantos anos voce deseja quitar a casa'))
l3 = float(input('qual seu salario atual'))
l4 = l1/l2
l5 = 0.3*l3
if l5>l4:
    print('seu empréstimo sera aprovado, e a pacela a ser paga por mes é {}'.format(l4))
else:
    print('seu emprestimo foi negado por conta da parcela ser maior que 30% do seu salario')