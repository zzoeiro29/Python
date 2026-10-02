num1 = int(input("digite um numero: "))
opcao = str(input("Quer continuar? [S/N]: "))
cont_num = 1
soma = maior = menor = media = num1
while opcao in "Ss":
    soma += num1
    num1 = int(input("digite um numero: "))
    #verificar se é maior ou menor
    if num1 > maior:
        maior = num1
    if num1 < menor:
        menor = num1
    opcao = str(input("Quer continuar? [S/N]: "))
    cont_num += 1
media = soma/cont_num
print("voce digitou {} numeros e a media foi {}".format(cont_num, media))
print("o maior numero foi {} e o menor foi {}".format(maior,menor))
