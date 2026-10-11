texto = input("Introduz uma string: ")
frequencia = {}
for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
print(frequencia)
for caractere, quantidade in frequencia.items():
    print(caractere, ":", quantidade)







