print("--" * 20)
print("Analisador de Triangulos")
print("--" * 20)
x = float(input("Primeiro segmento: "))
y = float(input("Segundo segmento: "))
z = float(input("Terceiro segmento: "))
if x + y > z and z + y > x and x + z > y:
    if x == y == z:
        print("Os segemntos acima formam um triangulo equilatero")
    elif x == y != z or y == z != x or z == x != y:
        print("Os segemntos acima formam um triangulo isoceles")
    elif x != y != z != x:
        print("Os segemntos acima formam um triangulo escaleno")
else:
    print("Os segemntos acima NAO PODEM FORMAR um triangulo")