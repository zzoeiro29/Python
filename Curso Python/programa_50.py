soma = 0
cont = 0
for c in range (0,6):
    x = int(input("digite o {} numero: ". format(c+1)))
    if ( x % 2 == 0):
        soma += x
        cont += 1
print("voce informou {} numeros pares e o soma foi {}".format(cont, soma))