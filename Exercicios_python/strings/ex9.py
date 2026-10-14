frase = input("Digite uma frase: ")
frase2 = input("Digite uma frase: ")
melhor = ""
for i in range(len(frase)):
    for j in range(i + 1, len(frase) + 1):
        pedaco = frase[i:j]
        if pedaco in frase2 and len(pedaco) > len(melhor): # se pedaco está em frase2 E é mais comprido que melhor:
            melhor = pedaco
print(melhor)