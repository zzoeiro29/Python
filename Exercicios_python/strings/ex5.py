frase = input("Digite uma frase: ")
melhor = ""
for i in range(len(frase)):
    atual = ""
    for letra in frase[:i]:
        if letra not in atual:
            atual += letra
        else:
            break
    if len(atual) > len(melhor):
        melhor = atual
print(melhor)




