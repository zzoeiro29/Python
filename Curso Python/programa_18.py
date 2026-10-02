from math import sin,cos,tan,radians
angulo = int(input("digite um angulo que voce deseja: "))
seno = sin(radians(angulo)) #bilioteca de seno
print("O angulo de {} tem o seno de {:.2f}".format(angulo, seno))
coseno = cos(radians(angulo)) #bilioteca de coseno
print("O angulo de {} tem o coseno de {:.2f}".format(angulo,coseno))
tangente = tan(radians(angulo)) #bilioteca de tangente
print("O angulo de {} tem a tangente de {:.2f}".format(angulo,tangente))