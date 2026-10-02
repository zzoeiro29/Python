from random import choice
al_1 = str(input("Digite o primeiro aluno: "))
al_2 = str(input("Digite o segundo aluno: "))
al_3 = str(input("Digite o terceiro aluno: "))
al_4 = str(input("Digite o quarto aluno: "))
lista = [al_1,al_2,al_3,al_4] # lista
escolhido = choice(lista) #random.choice escolhe aleatoriamante ou so choice
print("O aluno escolhido foi {}".format(escolhido))


