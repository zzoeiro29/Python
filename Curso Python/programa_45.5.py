from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print("Suas opçoes: ")
print("""
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
""")
jogador = int(input("Qual a sua jogada? "))
print("JO"); sleep(1)
print("KEN"); sleep(1)
print("PO!!")
print("-="*10)
print("computador jogou {}".format(itens[pc]))
print("jogador jogou {}".format(itens[jogador]))
if pc == 0:
    if jogador == 0 :
        print("empate")
    elif jogador == 1 :
        print("jogador venceu")
    elif jogador == 2 :
        print("computador venceu")
    else:
        print("burro")
elif pc == 1 :
    if jogador == 0 :
        print("computador venceu")
    elif jogador == 1 :
        print("empate")
    elif jogador == 2 :
        print("jogador venceu")
    else:
        print("burro")
elif pc == 2 :
    if jogador == 0 :
        print("jogador venceu")
    elif jogador == 1 :
        print("computador venceu")
    elif jogador == 2 :
        print("empate")
    else:
        print("burro")
print("-="*10)