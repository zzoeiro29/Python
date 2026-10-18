n = int(input("Informe um numero: "))
if n < 1:
    print("este numero nao e potencia de 2")
else:
    while n % 2 == 0:
        n = n // 2
if n == 1:
    print("este numero é potencia de 2")
else:
    print("este numero nao é potencia de 2")