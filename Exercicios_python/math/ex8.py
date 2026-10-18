n = int(input("Digite um numero: "))
binario = ""
if n == 0:
    binario = "0"
else:
    while n > 0:
        resto = n % 2         # resto de n a dividir por 2
        binario = str(resto) + binario
        n = n //2             # n dividido por 2 (divisão inteira)
print(binario)