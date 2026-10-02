#minha versao esta totalmente correta aura + ego
"""
Jogadores = dict()
lista = []
Jogadores["nome"] = str(input("Nome do jogador: "))
total = 0
partidas = int(input(f"Quantas partidas {Jogadores['nome']} jogou? "))
for c in range(0, partidas):
    gols = int(input(f"Quantos gols na partida {c}: "))
    Jogadores["gols"] = lista
    lista.append(gols)
    total += gols
Jogadores["total"] = total
print("-=" * 30)
print(Jogadores)
print("-=" * 30)
for k, v in Jogadores.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {Jogadores['nome']} jogou {partidas} partidas")
cont = 0
for l in lista:
    print(f"  => Na partida {cont}, fez {l} gols")
    cont += 1
print(f"Foi um total de {total} gols")
"""

#versao do gunabara
Jogadores = dict()
partidas = list()
Jogadores["nome"] = str(input("Nome do jogador: "))
tot = int(input(f"Quantas partidas {Jogadores['nome']} jogou? "))
for c in range(0, tot):
    partidas.append(int(input(f" Quantos gols na partida {c}: ")))
Jogadores["gols"] = partidas[:] # copiar a lista partidas pra meter no valor do gols
Jogadores["total"] = sum(partidas) # somar as partidas
print("-=" * 30)
print(Jogadores)
print("-=" * 30)
for k, v in Jogadores.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {Jogadores['nome']} jogou {len(Jogadores["gols"])} partidas")
for i, v in enumerate(Jogadores["gols"]):  # ver a lista
    print(f"  => Na partida {i}, fez {v} gols")
print(f"Foi um total de {Jogadores["total"]} gols")
