# Encontrar o segundo maior elemento da lista sem usar sort
def Segundo():
    l = []
    maior = 0
    segundo_maior = 0
    for c in range(1,6):
        n = int(input("Digite um numero: "))
        l.append(n)
        if c == 1:
            maior = n
        else:
            if n > maior:
                segundo_maior = maior
                maior = n
            elif n > segundo_maior:
                segundo_maior = n
    print(l)
    print(f"o segundo maior é {segundo_maior}")

Segundo()

