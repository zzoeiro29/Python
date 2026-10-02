soma = 0
media = 0
maior = 0
cont_mulher = 0
nome_antigo = str()
for p in range(1, 5):
    print("-" * 5, "{}º pessoa".format(p), "-" * 5)
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    Sexo = str(input("Sexo [M/F]: ")).upper().strip()
    #media
    soma += idade # soma = soma + idade
    #nome
    if p == 1 and Sexo == "M": # ou p == 1 and Sexo in "Mm"
        maior = idade
        nome_antigo = nome
    if idade > maior and Sexo == "M":
        maior = idade
        nome_antigo = nome
    #mulher com menos de 20 anos
    if Sexo == "F" and idade < 20:
        cont_mulher += 1
media = soma / 4
print("A media de idade do grupo é de {} anos".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maior, nome_antigo))
print("Ao todo sao {} mulheres com menos de 20 anos".format(cont_mulher))