x = 0 # ou x = cont = soma = 0
cont = 0
soma = 0
x = int(input("digite um numero: [999 para parar]: "))
while x < 999:
    soma += x
    cont += 1
    x = int(input("digite um numero: [999 para parar]: "))
print("voce digitou {} numeros e a soma entre eles foi {}".format(cont,soma))


