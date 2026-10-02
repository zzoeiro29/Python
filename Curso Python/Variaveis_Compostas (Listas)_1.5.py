valores = list() #funçao list
"""
valores.append(5)
valores.append(9)
valores.append(8) 
"""

#for cont in range(0, 5):
#    valores.append(int(input("Digite um valor: "))) #vai adicionar 5 vezes

"""
print("Os valores sao: ", end="")
for valor in valores:
    print(valor, end=" ")
"""

#for c, v in enumerate(valores):
#    print(f"Na posicao {c} encontrei o valor {v}")
#print("Chegeui ao final da lista")

#Ligaçao entre listas
a = [2,3,4,7]
b = a[:] # copia valores
# b = a  # faz uma ligaçao entres listas
b[2] = 8
print(f"lista A: {a}")
print(f"lista B: {b}")



