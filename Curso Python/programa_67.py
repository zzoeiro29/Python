while True:
    cont = 1
    numero = int(input("Quer ver a tabuada de qual valor? "))
    if numero < 0:
        print("programa encerrado. nao volte kkk")
        break
    while cont < 11:
        print(f"{numero} x {cont} = {numero * cont}")
        cont += 1
    # ou com for
    """
    for c in range(1, 11):
        print(f"{numero} x {cont} = {numero * cont}")
print("programa encerrado. nao volte kkk")
    """