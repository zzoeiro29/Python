frase = input("Digite uma frase: ")
atual = frase[0]
resultado = ""
cont = 1
for i in range(1, len(frase)):
    if frase[i] == atual:
        cont += 1
    else:
        resultado += atual
        resultado += str(cont)
        atual = frase[i]
        cont = 1
resultado += frase[-1]
resultado += str(cont)
print(resultado)

