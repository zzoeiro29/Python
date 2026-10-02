"""
cont = 1
while True: #ciclo infinito
    print(cont , "-> " , end="")
    cont += 1
print("fim")
"""
n = s = 0
while True:
    n = int(input("digite um numero: "))
    if n == 999:
        break
    s += n
#print(s)
# f strings
print(f"A soma vale {s}")
# format
#print("A soma vale{}".format(s))

