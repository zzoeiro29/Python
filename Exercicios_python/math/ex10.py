# minha versao
"""
x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
resultado = 0
if x > y:
    for i in range(x, x-(-y)-(-1)):
        resultado = i
else:
    for i in range(y, y-(-x)-(-1)):
        resultado = i
print(resultado)
"""

x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))

resultado = x
for i in range(y):
    resultado -= -1

print(resultado)