#Verificar se string é um palidromo
nome = str(input("Digite seu nome:"))
inverso = ""
for c in range( len(nome) -1, -1, -1):
    inverso += nome[c]
if inverso == nome:
    print(f"O {inverso} é um palindromo")
else:
    print(f"O {inverso} nao é um palindromo")