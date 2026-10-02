""" outra maneira
numeros = [ int(input("Digite um valor para a posiçao 0: ")),
            int(input("Digite um valor para a posiçao 1: ")),
            int(input("Digite um valor para a posiçao 2: ")),
            int(input("Digite um valor para a posiçao 3: ")),
            int(input("Digite um valor para a posiçao 4: "))]
"""


numeros = []# lista
#ou numeros = list()
""" Minha versao
for cont in range(0, 5):
    numeros.append(int(input(f"Digite um numero na posiçao {cont}: "))) # append adicionar
print("-=" *20)
print(f"voce digitou os valores {numeros}" )
maior = menor = numeros[0]
for v in numeros:
    if v > maior:
        maior = v
    elif v < menor:
        menor = v
print(f"O maior foi {maior} nas posiçaos ", end ="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i}...",end="")

print(f"\nO menor foi {menor} nas posiçaos ", end ="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i}...",end="")
"""
# versao gunabara
mai = 0
men = 0
for cont in range(0, 5):
    numeros.append(int(input(f"Digite um numero na posiçao {cont}: "))) # append adicionar
    if cont == 0:
        mai = men = numeros[cont]
    else:
        if numeros[cont] > mai:
            mai = numeros[cont]
        elif numeros[cont] < men:
            men = numeros[cont]
print("-=" *20)
print(f"voce digitou os valores {numeros}" )

print(f"O maior foi {mai} nas posiçaos ", end ="")
for i, v in enumerate(numeros):
    if v == mai:
        print(f"{i}...",end="")

print(f"\nO menor foi {men} nas posiçaos ", end ="")
for i, v in enumerate(numeros):
    if v == men:
        print(f"{i}...",end="")
