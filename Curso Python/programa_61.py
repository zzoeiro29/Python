""" Primiera maneira
print("gerador de PA")
print("-=" * 10)
x = int(input("Primeiro termo: "))
razao = int(input("Razao PA: "))
cont = 1
formula = 0
while cont <= 10:
    formula = x + (cont - 1) * razao
    print(formula, end= " --> ")
    cont += 1
print("fim")
"""
# segunda maneira
print("gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao PA: "))
#termo = primeiro nao sei pra que
cont = 1
while cont <= 10:
    print(primeiro, end= " --> ")
    primeiro += razao
    cont += 1
print("fim")