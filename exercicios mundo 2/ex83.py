#l1 = input('digite uma expressão com espaço entre os termos: ')
#num1 = l1.count('(')
#num2 = l1.count(')')
#if num1 == num2:
   # print('valida!')
#else:
    #print('invalida!')

lista_a = []
lista_b = []
e = input('digite a expressão: ')
for c in(e):
    if c == '(':
        lista_a.append(c)
    if c == ')':
        lista_b.append(c)
if len(lista_a) == len(lista_b):
    print('valida!!')
else:
    print('invalida!!')

