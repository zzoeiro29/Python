from random import randint
cont = 0
pc = randint(0,10)
print("Sou seu pc...")
print("Acabei de pensar em um numero entre 0 a 10.")
print("Sera que voce consegue adivinhar qual foi?")
"""
palpite = int(input("Qual é seu palpite: "))
while palpite != pc:
    if pc > palpite:
       print("Mais.. tente mais uma vez")
    elif pc < palpite:
        print("Mais.. tente mais uma vez")
    palpite = int(input("Qual é seu palpite: "))
    cont += 1
"""
#outra maneira
acertou = False
while not acertou:
    palpite = int(input("Qual é seu palpite: "))
    cont += 1
    if palpite == pc:
        acertou = True
    else:
        if palpite < pc:
            print("Mais.. tente mais uma vez")
        elif palpite > pc:
            print("Mais.. tente mais uma vez")
print("Acertou com {} tentativas".format(cont))
