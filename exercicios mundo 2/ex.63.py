primeiro_termo = int(input('digite um numero'))
segundo_termo = primeiro_termo
affs = primeiro_termo
l2 = 0
print(primeiro_termo)
print(segundo_termo)
while l2 != affs:
    terceiro_termo = primeiro_termo + segundo_termo
    print(terceiro_termo)
    l2 = l2 + 1
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
