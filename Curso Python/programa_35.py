print("--" * 20)
print("Analisador de Triangulos")
print("--" * 20)
x = float(input("Primeiro segmento: "))
y = float(input("Segundo segmento: "))
z = float(input("Terceiro segmento: "))
if x + y > z and z + y > x and x + z > y:
    print("Os segemntos acima PODEM FORMAR um triangulo")
else:
    print("Os segemntos acima NAO PODEM FORMAR um triangulo")
