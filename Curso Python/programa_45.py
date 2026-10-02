from random import randint
from time import sleep
print("Suas opçoes: ")
print("""
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
""")
opcao = int(input("Qual a sua jogada? "))
print("JO"); sleep(1)
print("KEN"); sleep(1)
print("PO!!")
pc = randint(0,2)
print("-="*10)
if opcao == 0 and pc == 2:
    print("Computador jogou Tesoura")
    print("Jogador jogou Pedra")
    print("Jogador vence")
elif opcao == 2 and pc == 0:
    print("Jogador jogou Pedra")
    print("Jogador jogou Tesoura")
    print("Jogador perde")
elif opcao == 1 and pc == 0:
    print("Computador jogou pedra")
    print("Jogador jogou papel")
    print("Jogador vence")
elif opcao == 0 and pc == 1:
    print("Computador jogou papel")
    print("Jogador jogou pedra")
    print("Jogador perde")
elif opcao == 1 and pc == 2:
    print("Computador jogou tesoura")
    print("Jogador jogou papel")
    print("Jogador perde")
elif opcao == 2 and pc == 1:
    print("Computador jogou papel")
    print("Jogador jogou tesoura")
    print("Jogador vence")
elif opcao == 0 and pc == 0:
    print("Computador jogou Pedra")
    print("Jogador jogou Pedra")
    print("Empatou")
elif opcao == 1 and pc == 1:
    print("Computador jogou papel")
    print("Jogador jogou papel")
    print("Empatou")
elif opcao == 2 and pc == 2:
    print("Computador jogou Tesoura")
    print("Jogador jogou Tesoura")
    print("Empatou")
else:
    print("jogou oq arrombado?")
print("-="*10)