def torres (n, origem, destino, apoio):
    if n == 1:
        print(f"Mover disco {n} de {origem} para {destino}")
    else:
        torres(n-1, origem, apoio, destino)
        print(f"Mover disco {n} de {origem} para {destino}")
        torres(n-1, apoio, destino, origem)
num = int(input("Digite o numero de discos: "))
torres(num, "A", "C", "B")
