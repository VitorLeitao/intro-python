times = ('flamengo', 'vorax', 'red canids', 'loud', 'pain', 'kabum')


print('\nA)os tres primeiros colocados são: ')
for c in range(0, 3):
    print(f'{c + 1}° -> {times[c]}')


print('\nB) os tres ultimos times são: ')
for c in range(3, 6):
    print(f'{c + 1}° -> {times[c]}')


print('\nC) os times em ordem alfabética são: ')
print(sorted(times))


print('\nD) em qual posição a red canids está?')
posição_ini = int(times.index('red canids'))
print(posição_ini + 1)



