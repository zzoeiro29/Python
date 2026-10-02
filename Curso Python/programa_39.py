from datetime import date
nasc = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual-nasc #ou 2026
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, ano_atual))
if idade < 18:
    print("Ainda faltam {} anos para o alistamento".format(18-idade))
    print("Seu alistamento sera em {}".format(nasc+(18-idade)))
elif idade > 18:
    print("Voce deveria ter se alistado ha {} anos".format(idade-18))
    print("Seu alistamento foi em {}".format(nasc+18))
else:
    print("Voce tem que se alistar")