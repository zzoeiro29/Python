"""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais numero: "))
n4 = int(input("Digite o ultimo numero: "))
tupla = (n1,n2,n3,n4)
"""
num = (int(input("Digite um numero: ")),
        int(input("Digite um numero: ")),
        int(input("Digite um numero: ")),
        int(input("Digite um numero: ")))
print(f"Voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
print(f"O valor 3 apareceu na posiçao {num.index(3)}º" if 3 in num else "O valor 3 nao apareceu") # se 3 estiver dentro da tupla num
print(f"Os valores digirados pares foram: ", end="")
for c in num:
    if c % 2 == 0:
        print(f"{c}", end=" ")

