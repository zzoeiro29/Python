#Remover elementos duplicados de uma lista mantendo a ordem original.
l = []
d = []
for c in range(1,6):
    n = int(input("Digite um numero: "))
    l.append(n)
for n in l:
    if n not in d:
        d.append(n)
print(d)

