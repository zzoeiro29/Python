#inverter uma string sem usar [::-1]
nome = input("Digite seu nome:")
inverso = ""
for c in range(len(nome) -1, -1, -1):
    inverso += nome[c]
print(inverso)