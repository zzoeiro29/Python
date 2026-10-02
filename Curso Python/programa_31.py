D = float(input("digite a distancia de uma viagem em km "))
print("voce esta a começar uma viagem de {}km".format(D))
#segunda maneira
preco = D * 0.50 if D <= 200 else D * 0.45 #if simplificado
#primeira maneira
"""
if D <= 200:
    print("e o preço da sua passagem sera de R${:.2f}".format(D * 0.5)) #preço viagem mais curta 0.50 centimos
else:
    print("e o preço da sua passagem sera de R${:.2f}".format(D * 0.45)) #preço viagem mais longa 0.45 centimos
"""
print("e o preço da sua passagem sera de R${:.2f}".format(preco))