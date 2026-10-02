from math import radians
from random import randint
from time import sleep
from operator import itemgetter # organizar dicionario

""" minha versao metade kkk
Jogadores = {}
print("Valores sorteados: ")
Jogadores["Jogador1"] = randint(1, 6)
Jogadores["Jogador2"] = randint(1, 6)
Jogadores["Jogador3"] = randint(1, 6)
Jogadores["Jogador4"] = randint(1, 6)
Organizar.append(Jogadores.copy())
for k, v in Jogadores.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
print("-=" * 30)
print("  == Ranking de jogadores == ")
"""

jogo = {"Jogador1": randint(1, 6),
        "Jogador2": randint(1, 6),
        "Jogador3": randint(1, 6),
        "Jogador4": randint(1, 6)}
ranking = dict()
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
#por ordem é com reverse , sem ordem é sem o reverse
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # 0 ordem de chave , 1 ordem de valor
print("  == Ranking de jogadores == ")
for i, v in enumerate(ranking):
    print(f"  {i+1}º lugar foi {v[0]} com {v[1]}")