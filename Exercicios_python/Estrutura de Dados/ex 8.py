matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transporte = []

for i in range(3):
    coluna = []
    for linha in matriz:
        coluna.append(linha[i])
    transporte.append(coluna)
print(transporte)