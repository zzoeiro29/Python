from datetime import date
cont_adultos = 0
cont_menores = 0
for c in range(0,7):
    ano_nasc = int(input("Em que ano a {}º pessoa nasceu: ".format(c+1)))
    if date.today().year - ano_nasc >= 21: #  date.today().year ou 2026
        cont_adultos += 1
    else:
        cont_menores += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(cont_adultos))
print("Ao todo tivemos {} pessoas menores de idade".format(cont_menores))