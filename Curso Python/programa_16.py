from math import trunc #biblioteca matematica
x = float(input("digite um numero: "))
# primeira maneira: print("o balor digitado foi {} e a suua porçao inteira é {}".format(x, int(x)))
# segunda maneira:
print("o balor digitado foi {} e a suua porçao inteira é {}".format(x, trunc(x))) #trunc so mostra a parte inteira