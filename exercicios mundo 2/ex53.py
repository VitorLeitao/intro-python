l1 = input('digite uma frase').strip().lower().split()
l2 = ''.join(l1)
if l2 == l2[::-1]:
    print('é um palindromo')
else:
    print('nao é um palindromo')
