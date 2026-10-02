#for = quando sei o limite
"""
for c in range(1,5):
    n = int(input("digite um valor: "))
print("fim")
"""
# while = quando n sei o limite ou um valor defenido
"""
r = "S"
while r == "S":
    n = int(input("digite um valor: "))
    r = str(input("quer continuar? [S/N]: ")).upper()
print("fim")
"""
n = 1
par = 0; impar = 0
while n != 0:
    n = int(input("digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("voce digitou {} numeros pares e {} numeros impares ".format(par, impar))

print("fim")

