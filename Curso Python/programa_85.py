"""
lista = list()
pares = list()
impares = list()
for c in range(1, 8):
    n  = int(input(f"Digite o {c}º valor: "))
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    lista.append(pares[:])
    lista.append(impares[:])
print("-=" *30)
pares.sort() #organizar do maior pro menor
print(f"Os valores pares digitados foram: {pares}")
impares.sort()
print(f"Os valores impares digitados foram: {impares}")
"""
# versao gunabara certa
n = [ [] , [] ]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        n[0].append(valor)
    elif valor % 2 == 1:
        n[1].append(valor)
print("-=" *30)
n[0].sort()
n[1].sort()
print(f"Os valores pares digitados foram: {n[0]}")
print(f"Os valores impares digitados foram: {n[1]}")

