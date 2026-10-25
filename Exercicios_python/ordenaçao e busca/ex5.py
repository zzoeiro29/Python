def quick_sort(lista):
    if len(lista) <= 1:                      # caso base: quando devolve a lista como está?
        return lista
    pivo = lista[0]
    menores = []
    maiores = []
    for numero in lista[1:]:     # percorre todos menos o pivô
        if numero < pivo:                  # numero é menor que o pivô?
            menores.append(numero)
        else:
            maiores.append(numero)
    return quick_sort(menores) + [pivo] + quick_sort(maiores)    # quick_sort dos menores + pivô + quick_sort dos maiores
Lista = [ 5,3,1,8 ]
print(quick_sort(Lista))

