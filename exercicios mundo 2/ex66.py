s = num = 0
while True:
    l1 = float(input('digite um numero, 999 para parar: '))
    if l1 == 999:
        break
    s = s + l1
    num = num + 1
print(f'a soma dos numeros é {s} e a quantidade {num}')