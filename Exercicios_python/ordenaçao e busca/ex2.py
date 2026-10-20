n = int(input("Quantos numeros? "))
lista = []
for c in range(n):
    lista.append(int(input("Digite um numero: ")))
for i in range(0, len(lista) ):
    pos_menor = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[pos_menor]:
            pos_menor = j
    lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
print(lista)