frase1 = input("Digite uma frase: ")
frase2 = ""
for letra in frase1:
    if letra not in frase2:
        frase2+=letra
print(frase2)
