listagem = (
           "Lapis" , 1.75,
           "Borracha" , 2,
           "Caderno" , 15.90,
           "Estojo",25,
           "Transferidor", 4.20,
           "Compaso", 9.99,
           "mochila", 120.32,
           "Canetas", 22.30,
           "Livro", 34.90)
print("-" *40)
# antes de centralizar ou outra coisa por :
print(f"{"LISTAGEM DE PREÇOS":^40}") # centralizado ^
print("-" *40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end ="") # ha esquerda <
    else:
        print(f"R${listagem[pos]:>10}") # ha direita >
print("-" *40)