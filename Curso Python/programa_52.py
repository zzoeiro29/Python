""" Minha versao
n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n+1):
    if c % 1 == 0 and n % c == 0:
        print("\033[33m {}".format(c), end=" " "\033[m" )
        cont += 1
    else:
        print("\033[31m {}".format(c), end=" " "\033[m")
print("\nO numero {} foi divisivel {} vezes".format(n, cont))
if cont == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele NAO é primo")
"""

#outra versao
n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n+1):
    if c % 1 == 0 and n % c == 0:
        print("\033[33m ", end="")
        cont += 1
    else:
        print("\033[31m ", end="")
    print("{}".format(c), end="")
print("\n\033[mO numero {} foi divisivel {} vezes".format(n, cont))
if cont == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele NAO é primo")