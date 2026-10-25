def juntar(esq, direita):
    resultado = []
    i = 0
    j = 0
    while i < len(esq) and j < len(direita):
        if esq[i] <= direita[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado = resultado + esq[i:]
    resultado = resultado + direita[j:]
    return resultado

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esq = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return juntar(esq, direita)

Lista = [5,8,1,7]
print(merge_sort(Lista))