def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

def fatorial_recursivo(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial_recursivo(n-1)

numero = int(input("Digite um numero: "))
print(fatorial_recursivo(numero))
print(fatorial_iterativo(numero))

