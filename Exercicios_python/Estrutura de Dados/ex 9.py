dicionario = {}
nome = ["joao", "Maria"]
idade = [15, 16]
for c in range(len(nome)):
    dicionario[nome[c]] = idade[c]
for k, v in dicionario.items():
    print(f"{k} = {v}")
