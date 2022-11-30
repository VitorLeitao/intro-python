n = int(input('Quantos numeros deve ter na sequencia? '))
num_1 = 1
num_2 = 1
print(num_1)
print(num_2)
for c in range(0, n):
    num_prox = num_1 + num_2
    num_1 = num_2
    num_2 = num_prox
    print(num_prox)