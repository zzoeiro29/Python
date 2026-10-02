def fatorial(n, show = False):
    """
    --> Calcula a merda do fatorial
    :param n: n é um, filha da puta
    :param show: (opcional) mostra o valor do fatorial
    :return: e o return é outro morra

    Fatorial de n
    f = 1
    for i in range (n,0,-1):
        f *= i
    return f
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            if i>1:
                print(f"{i} x", end=" ")
            else:
                print(" = ", end=" ")
        f *= i
    return f

print(fatorial(5, True))
help(fatorial)
