#minha versao
"""
def jogador(Nome, golos):
    if Nome == "":
        return f"O jogador <desconhecido> fez {golos} gol(s) no campeonato."
    elif golos == "":
        return f"O jogador {Nome} fez 0 gol(s) no campeonato."
    elif Nome == "" and golos == "":
        return "O jogador <desconhecido> fez 0 gol(s) no campeonato."
    else:
        return f"O jogador {Nome} fez {golos} gol(s) no campeonato."



nome = str(input("Nome do jogador: "))
n = str(input("Número de Gols: "))
print(jogador(nome, n))
"""
#versao gunabara

def jogador(Nome="<desconhecido>", golos=0):
    print(f"O jogador {Nome} fez {golos} gol(s) no campeonato.")


nome = str(input("Nome do jogador: "))
n = str(input("Número de Gols: "))
if n.isnumeric():
    n = int(n)
else:
    n = 0

if nome.strip() == "":
    jogador(golos=n)
else:
    jogador(nome,n)
