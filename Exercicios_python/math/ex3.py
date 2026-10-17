num1 = int(input("digite um numero inteiro: "))
num2 = int(input("digite outro numero inteiro: "))

while num2 != 0:
    resto = num1 % num2
    num1 = num2
    num2 = resto

print("MDC:", num1)