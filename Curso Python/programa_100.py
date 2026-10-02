from random import randint
from time import sleep
#minha versao
"""
valores = [randint(1, 10),
           randint(1, 10),
           randint(1, 10),
           randint(1, 10),
           randint(1, 10)]
def sortear():
    print(f"Sorteando {len(valores)} valores da lista: ", end="")
    for v in valores:
        print(v, end= " ")
    print("PRONTO!")

def somar_pares():
    somar = 0
    for v in valores:
        if v % 2 == 0:
            somar += v
    print(f"Somando os valores pares de {valores}, temos {somar}")

sortear()
somar_pares()
"""
#versao gunabara
def sortear(lista):
    print(f"Sorteando {len(lista)} valores da lista: ", end="")
    for cont in range(0, 5):
        n = (randint(1, 10))
        lista.append(n)
        print(f"{n}", end=" ")
        sleep(0.3)
    print("PRONTO!")

def somar_pares(lista):
    somar = 0
    for v in lista:
        if v % 2 == 0:
            somar += v
    print(f"Somando os valores pares de {lista}, temos {somar}")

numeros = list()
sortear(numeros)
somar_pares(numeros)

