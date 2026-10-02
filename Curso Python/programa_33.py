x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
z = int(input("Terceiro valor: "))
#primeira maneira
#menor
"""
if x < y and x < z:
    print("O menor valor digitado é: ", x)
elif y < x and y < z:
    print("O menor valor digitado é: ", y)
elif z < x and z < y:
    print("O menor valor digitado é: ", z)

#maior
if x > y and x > z:
    print("O maior valor digitado é: ", x)
elif y > x and y > z:
    print("O maior valor digitado é: ", y)
elif z > x and z > y:
     print("O menor valor digitado é: ", z)
"""

#segunda maneira
menor = x
if y < x and y < z:
    menor = y
elif z < x and z < y:
    menor = z
print("O menor valor digitado é: ", menor)
maior = x
if y > x and y > z:
    maior = y
elif z > x and z > y:
    maior= z
print("O maior valor digitado é: ", maior)

