num = int(input('Montar a tabuada de: '))
comeco = int(input('Começar por: '))
final = int(input('Terminar em: '))
if final >= comeco:
    for c in range(comeco, final + 1):
        resultado = num * c
        print(f'{num} * {c} = {resultado}')
else:
    print(f'ERROR')
