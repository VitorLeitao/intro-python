num_1 = 1
num_2 = 1
print(num_1)
print(num_2)
while True:
    num_prox = num_1 + num_2
    print(num_prox)
    num_1 = num_2
    num_2 = num_prox
    if num_prox > 500:
        break
