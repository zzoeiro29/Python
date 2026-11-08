lista = []
acertou = 0
t = int(input("digite um numero de 1 a 4 para indicar o cha: "))
a = int(input("concorrente digite um numero de 1 a 4: "))
b = int(input("concorrente digite um numero de 1 a 4: "))
c = int(input("concorrente digite um numero de 1 a 4: "))
d = int(input("concorrente digite um numero de 1 a 4: "))
e = int(input("concorrente digite um numero de 1 a 4: "))
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
for i in range(0, len(lista)):
    if t == lista[i]:
        acertou += 1
print(acertou)