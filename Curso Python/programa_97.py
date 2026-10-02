#minha versao
"""
def traco(msg):
    print("-" * len(msg))

escrita = "Gustavo gunabara"
traco(escrita)
print(escrita)
traco(escrita)
escrita = "Curso em Python no youtube"
traco(escrita)
print(escrita)
traco(escrita)
escrita = "Cev"
traco(escrita)
print(escrita)
traco(escrita)
"""

#versao gunabara

def escrita(msg):
    tam = len(msg) + 4
    print("-" * tam)
    print(f"  {msg}")
    print("-" * tam)

escrita("Gustavo gunabara")
escrita("Curso em Python no youtube")
escrita("Cev")

