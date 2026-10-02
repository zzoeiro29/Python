"""

r : leitura do arquivo  read
w :  escrita ( sobrescreve o conteudo existente) write
a : anexa ao final do arquivo append
r+ : leitura e escrita

"""

#metdodo antigo
"""
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read() #le
print(conteudo)
arquivo.close() # fecha
"""

with open("exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
