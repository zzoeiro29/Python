lista = [4, 2, 2, 8, 3, 3, 1]
maior = max(lista) #maior numero
contagem = [0] * (maior + 1) #0 oitos
ordenada = []

for numero in lista:
    contagem[numero] += 1

for i in range(maior + 1):
    for j in range(0, contagem[i]):      # quantas vezes?
        ordenada.append(i)  # o quê?

print(ordenada)