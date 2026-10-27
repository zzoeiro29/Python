def descer(lista, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and lista[esq] > lista[maior]:
        maior = esq
    if dir < n and lista[dir] > lista[maior]:
        maior = dir
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        descer(lista, n, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        descer(lista, n , i)
    for j in range(n - 1,  0 , -1):
        lista[0], lista[j] = lista[j], lista[0]
        descer(lista, j, 0)
lista = [2, 9, 7, 4]
heap_sort(lista)
print(lista)