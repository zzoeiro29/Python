# nem tenta cara
N = int(input("Digite o limite de numero ate N: "))
crivo = [True] * (N + 1)
for i in range (2, N + 1):
    if crivo[i]:
        for m in range(i * 2, N + 1, i):
            crivo[m] = False
primos = []
for i in range(2, N + 1):
    if crivo[i]:
        primos.append(i)
print(primos)