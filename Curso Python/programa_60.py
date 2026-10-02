""" primeira forma

from math import factorial
x = int(input("Digitre um numero para \ncalacular o seu fatorial: "))
f = factorial(x)
print("O factorial de {} de {}.".format(x, f))
"""

#segunda maneira
x = int(input("Digitre um numero para \ncalacular o seu fatorial: "))
c = x
f = 1
print("Calculando {}! = ".format(x), end= "")
while c > 0:
    print("{} ".format(c), end="")
    print("x " if c > 1 else " = ", end="")
    f *= c
    c-=1
print(f)

""" terceira maneira com o for ate 5
f = 1
for c in range(1, 6):
    print("{} ".format(c), end="")
    print("x " if c != 5 else "= ", end="")
    f *= c
    c -= 1
print(f)
"""