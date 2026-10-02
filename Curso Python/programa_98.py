from time import sleep
#minha versao (eu vou ganhar)
"""
def um():
    print("-=" * 30)
    print("Contagem de 1 ate 10 de 1 em 1")
    for i in range(1,11,1):
        print(i , end=" ")
        sleep(0.3)
    print("FIM!")
    print("-=" * 30)

def dois():
    print("Contagem de 10 ate 0 de 2 em 2")
    for i in range(10,-1,-2):
        print(i , end=" ")
        sleep(0.3)
    print("FIM!")
    print("-=" * 30)

def contagem(x,y,z):
    print(f"Contagem de {x} ate {y} em {z}")
    if z < 0:
        for i in range(x,y-1,z):
            print(i, end=" ")
            sleep(0.3)
        print("FIM!")
    if z >= 0:
        for i in range(x,y+1,z):
            print(i, end=" ")
            sleep(0.3)
        print("FIM!")


um()
dois()
print("Agora é sua vez de personalizar a contagem")
inicio = int(input("Inicio: "))
Fim = int(input("Fim: "))
Passo = int(input("Passo: "))
contagem(inicio,Fim,Passo)
"""

#versao gunabara -_-
def contador (i,f,p):
    print("-=" * 20)
    print(f"Contagem de {i} ate {f} em {p} em {p}")
    cont = i
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        while cont <= f:
            print(f"{cont} ",end=" ")
            sleep(0.3)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ",end=" ")
            sleep(0.3)
            cont -= p
        print("FIM!")


#Programa principal
contador(1,10,1)
contador(10,0,2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem")
inicio = int(input("Inicio: "))
Fim = int(input("Fim: "))
Passo = int(input("Passo: "))
contador(inicio,Fim,Passo)