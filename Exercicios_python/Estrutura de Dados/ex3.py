#Ordenar uma lista sem usar Funções de ordenação.
def Ordenar():
    lista = []

    for c in range(1, 6):
        n = int(input("Digite um número: "))
        lista.append(n)

    # Ordenação pelo método da bolha
    for i in range(len(lista)):
        for j in range(len(lista) -1 -i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux


    print(f"Lista ordenada {lista}")


Ordenar()

