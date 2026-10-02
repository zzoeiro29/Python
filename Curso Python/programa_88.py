from random import randint
from time import sleep
# Minha versao incompleta -_-
Jogo = []
print("-" * 20)
print("Jogo Na mega Sena".center(20) )
print("-" * 20)
jogos = int(input("Quantos jogos voce quer sortear? "))
print("-=" * 5 , f"Sorteando {jogos} jogos" ,"-=" * 5 )
c = 1
for c in range(jogos):
    sleep(1)
    Jogo.append(randint(1, 60))
    Jogo.append(randint(1, 60))
    Jogo.append(randint(1, 60))
    Jogo.append(randint(1, 60))
    Jogo.append(randint(1, 60))
    Jogo.sort()
    print(f"Jogo {c+1}: {Jogo}")
    Jogo.clear()
print("-=" * 5 , " < BOA SORTE > " , "-=" * 5)

#versao gunabara
"""
lista = []
jogos = []
print("-" * 20)
print("Jogo Na mega Sena".center(20) )
print("-" * 20)
Quantidade = int(input("Quantos jogos voce quer sortear? "))
tota = 1
while tota <= Quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tota += 1
print("-=" * 5 , f"Sorteando {Quantidade} jogos" ,"-=" * 5 )
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print("-=" * 5 , " < BOA SORTE > " , "-=" * 5)
"""


