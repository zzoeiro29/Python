"""
brasil = [] #lista
estado1  = {"uf":"Rio de Janeiro",
            "sigla":"RJ" }
estado2  = {"uf": "Sao paulo",
            "sigla": "SP" }
brasil.append(estado1)
brasil.append(estado2)
#print(brasil[0]) # estado 1
#print(brasil[1]) # estado 2
print(brasil[0]["uf"]) # Rio de janeiro
print(brasil[1]["sigla"]) #SP
"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Informe Unidade federativa: "))
    estado["sigla"] = str(input("Informe o Sigla: "))
    brasil.append(estado.copy()) # copiar
for e in brasil: # for pra lista
    for k, v in e.items(): # for pra dicionario
        print(f"{k} = {v}")
