#minha versao
"""
valores = []
while True:
    n = int(input("Digite um numero: "))
    valores.append(n)
    resp = str(input("Deseja continuar? [S/N] ")).upper()
    if resp == "N":
        break
print("-=" * 30)
print(f"A lista completa é: {valores}")
pares = []
impares = []
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    if valores[c] % 2 != 0:
        impares.append(valores[c])
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")
"""
#minha guanabara
valores = []
while True:
    n = int(input("Digite um numero: "))
    valores.append(n)
    resp = str(input("Deseja continuar? [S/N] ")).upper()
    if resp == "N":
        break
print("-=" * 30)
print(f"A lista completa é: {valores}")
pares = []
impares = []
for i, n in enumerate(valores):
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")