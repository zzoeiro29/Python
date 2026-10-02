#pilha
# o primeiro entra primeiro e o ultimo sai primeiro
def push(l):
    n = int(input("digite um valor:"))
    l.append(n)


def popes(l):
    #l.remove(l[-1])
    l.pop()

lista = []
while True:
    print(lista)
    print("1- push")
    print("2- pop")
    o = int(input("Digite a opçao: "))
    if o == 1:
        push(lista)
    elif o == 2:
        popes(lista)
    else:
        break


