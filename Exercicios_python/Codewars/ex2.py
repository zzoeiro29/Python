def filter_list(l):
    resultado = []
    for i in l:
        if type(i) == int: # ou usar o isinstance(i, int) i é do tipo int?"
            resultado.append(i)
    return resultado
lista = [1,2,"a","b"]
print(filter_list(lista))