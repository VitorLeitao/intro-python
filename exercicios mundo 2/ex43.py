l1 = float(input('digite seu peso:'))
l2 = float(input('digite sua altura, em metro:'))
l3 = float(l1/l2**2)
if l3 < 18.5:
    print('o individuo esta abaixo do peso')
elif 18.5 <= l3 < 25:
    print('o individuo esta no peso ideal')
elif 25 <= l3 < 30:
    print('o individuo esta com sobrepeso')
elif 30 <= l3 < 40:
    print('o individuo esta com obesidade')
else:
    print('o individuo esta com obesidade morbida')



