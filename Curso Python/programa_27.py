n = str(input("Digite seu nome: ")).strip()
nome = n.split() # separa os indices
print("prazer em te conhecer")
print("Seu primeiro nome é", nome[0])
print("Seu ultimo nome é", nome[len(nome)-1])