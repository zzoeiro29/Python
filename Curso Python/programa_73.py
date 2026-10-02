print("-" * 20)
Times = (
    "Corinthians", "Botafogo", "Palmeiras", "Flamengo",
    "Fortaleza", "Internacional", "São Paulo", "Cruzeiro",
    "Bahia", "Vitória", "Vasco da Gama",  "Juventude", "Grêmio",
    "Fluminense", "Atlético-MG", "RB Bragantino", "Santos",
    "Mirassol", "Sport", "Ceará",
)
print("Liste de times do Brasileirao: ", Times)
print("-" * 20)
print("Os primeiros 5 colocados:", Times[:5])
print("Os ultimos 4 colocados:", Times[16:]) # ou Times[-4:]
print("Times por ordem alfabetica: ", sorted(Times)) #deixa por ordem alfabetica
print(f"O Cruzeiro esta na {Times.index("Cruzeiro")+1}º posiçao") # minha maneira mais ou menos: {len(Times[7])}