from math import hypot
x = float(input("um cateto: "))
y = float(input("outro cateto: "))
#primeira maneira
#h = ( (x**2) + (y**2) ) ** (1/2) #potencia e raiz quadrada
#segunda maneira
h = hypot(x,y)  #biblioteca
print("A hipotenusa vai medir {:.2f}".format(h))
