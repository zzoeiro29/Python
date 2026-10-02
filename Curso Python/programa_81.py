valores = []
while True:
    n = int(input("Digite um valor: "))
    valores.append(n)
    res = " "
    while res not in "SN":
        res = str(input("Deseja continuar? [S/N] ")).upper()
    if res == "N":
        break
print("-=" * 30)
print(f"Voce digitou {len(valores)} elementos")
valores.sort(reverse=True)
print(f"Os valores em ordem descrescente sao {valores}")
if 5 in valores:
    print("O valor 5 foi encontrado na lista")
else:
    print("O valor 5 nao foi encontrado na lista")

