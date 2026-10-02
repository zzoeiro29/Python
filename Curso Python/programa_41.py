from datetime import date
ano = int(input("Qual o ano de nascimento: "))
idade = date.today().year - ano
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("nadador mirim")
elif idade <= 14:
    print("nadador infantil")
elif idade <= 19:
    print("nadador junior")
elif idade <= 25:
    print("nadador senior")
else:
    print("nadador master")