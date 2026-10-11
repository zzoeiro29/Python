#primeira forma
#nome = input("Qual o seu nome?")
#print(nome.upper().replace("A","-" ).replace("O","-").replace("E","-").replace("I","-").replace("U","-"))

#segunda
nome = str(input("Digite seu nome: ")).upper()
nome2 = ""
for letra in nome:
    if letra in "AEIOU":
        letra = "-"
        nome2 += letra
    else:
        nome2 += letra
print(nome2)



