# abrir aquivo escrever algo nele
#with open("ex1.txt", "w") as arquivo:
#    arquivo.write("linha 1")

#ler e exibir as 3 primeiras linhas
#with open("ex1.txt", "r") as arquivo:
#    print(arquivo.read())

#adicione uma nova mensagem ao final do arquivo
with open("ex1.txt", "a") as arquivo:
    arquivo.write("\nAcabou o exercicio")