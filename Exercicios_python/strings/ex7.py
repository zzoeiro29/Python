texto = input("Introduz um palavara: ")
texto2 = input("Introduza um anagrama: ")
cont = 0
frequencia = {}
frequencia2 = {}
for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
for caractere2 in texto2:
    if caractere2 in frequencia2:
        frequencia2[caractere2] += 1
    else:
        frequencia2[caractere2] = 1
if frequencia == frequencia2:
    print("é um anagrama")
else:
    print("nao é")

