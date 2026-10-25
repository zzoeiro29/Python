n = int(input("Quantos numeros? "))
lista = []

for c in range(n):
    lista.append(int(input("Digite um numero: ")))
for i in range(1, len(lista)):
    atual = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        j = j - 1
print(lista)
