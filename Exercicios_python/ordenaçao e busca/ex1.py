n = int(input("Quantos numeros? "))
lista = []
for c in range(n):
    lista.append(int(input("Digite um numero: ")))
for i in range(0, len(lista) ):
    for j in range(len(lista) - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)