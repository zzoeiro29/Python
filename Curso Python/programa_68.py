from random import randint
pc = randint(0, 10)
print("-=" * 30)
print("VAMOS JOGAR PAR OU IMPAR")
print("-=" * 30)
# primeira soluçao (a minha)
"""
cont2 = 0
while True:
    cont = 1
    jogador = int(input("digite um valor: "))
    escolha = str(input("Par ou impar? [P/I] "))
    F = jogador + pc
    print("-" * 20)
    if F % 2 == 0:
        print(f"Voce jogou {jogador} e o computador jogou {pc}. Total de {jogador + pc} deu par.")
        if escolha in "Pp":
            print("Voce ganhou!")
            cont2 += 1
        else :
            print("Voce perdeu!")
            cont -= 1
    elif F % 2 == 1:
        print(f"Voce jogou {jogador} e o computador jogou {pc}. Total de {jogador + pc} deu impar.")
        if escolha in "Ii":
            print("Voce ganhou!")
            cont2 += 1
        else :
            print("Voce perdeu!")
            cont -= 1
    print("-" * 20)
    if cont == 0:
        print(f"GAME OVER! voce ganhou {cont2} vezes")
        break
    print("vamos jogar novamente...")
"""
#versao guanabara
v = 0
while True:
    cont = 1
    jogador = int(input("digite um valor: "))
    total = jogador + pc
    tipo = " "
    print("-" * 20)
    while tipo not in "PI":
        tipo = str(input("Par ou impar? [P/I] ")).upper().strip()[0]
    print(f"Voce jogou {jogador} e o computador jogou {pc}. Total de {jogador + pc}. " , end="")
    print("Deu par" if total % 2 == 0 else "Deu impar")
    if tipo == "P":
        if total % 2 == 0:
            print(f"Voce ganhou!")
            v+=1
        else:
            print("Voce perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print(f"Voce ganhou!")
            v+=1
        else:
            print("Voce perdeu!")
            break
    print("-" * 20)
    print("vamos jogar novamente...")
print(f"GAME OVER! voce ganhou {v} vezes")