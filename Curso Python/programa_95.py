Jogadores = dict()
partidas = list()
time = list()
""" QUASE CERTO minha versao
cont = 0
while True:
    Jogadores.clear()
    Jogadores["cod"] = cont
    Jogadores["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {Jogadores['nome']} jogou? "))
    for c in range(0, tot):
        partidas.append(int(input(f" Quantos gols na partida {c}: ")))
    Jogadores["gols"] = partidas[:] # copiar a lista partidas pra meter no valor do gols
    Jogadores["total"] = sum(partidas) # somar as partidas
    time.append(Jogadores.copy())
    res = str(input("Quer continuar? [S/N]")).upper().strip()
    cont += 1
    while res not in "SN":
        res = str(input("Quer continuar? [S/N]")).upper().strip()
    if res == "N":
        break
print("-=" * 30)
print(f"{"cod":<2}" , f"{"nome":>5}" , f"{"gols":>8}" , f"{"Total":>10}")
print("-" * 30)
for j in time:
    gols_str = str(j['gols'])
    print(f"{j["cod"]}  {j['nome']:>5} {gols_str:>7} {j['total']:>8}")
print("-" * 30)
jogo = 0
while True:
    n = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if n == Jogadores["cod"]:
        for i, v in enumerate(Jogadores["gols"]):  # ver a lista
            print(f"  => Na partida {i}, fez {v} gols")
    print("-" * 30)
    if n == 999:
        break
"""
while True:
    Jogadores.clear()
    Jogadores["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {Jogadores['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f" Quantos gols na partida {c+1}: ")))
    Jogadores["gols"] = partidas[:] # copiar a lista partidas pra meter no valor do gols
    Jogadores["total"] = sum(partidas) # somar as partidas
    time.append(Jogadores.copy())
    while True:
        res = str(input("Quer continuar? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if res == "N":
        break
print("-=" * 30)
print("cod" , end= "")
for i in Jogadores.keys():
    print(f" {i:<15}", end= "")
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f"{k:>3}", end= "")
    for d in v.values():
        print(f" {str(d):<15}", end= "")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! nao existe esse jogador com codigo {busca}.")
    else:
        print(f"-- Levantamento do jogador {time[busca]['nome']}")
        for i, g in enumerate(time[busca]["gols"]):
            print(f"   No jogo {i+1} fez {g} gols")
    print("-" * 40)
print("NAO VOLTE NUNCA MAIS")


