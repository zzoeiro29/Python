n = int(input("Digite um numero: "))
lista = [1, 3, 5, 7, 9, 11, 13]
inicio = 0
fim = len(lista)-1
posicao = -1
while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == n:
        posicao = meio
        break
    elif lista[meio] > n:
        fim = meio - 1
    elif lista[meio] < n:
        inicio = meio + 1
if posicao != -1:
    print(f"Encontrado na posiçao {posicao}")
else:
    print("Nao encontrado")

