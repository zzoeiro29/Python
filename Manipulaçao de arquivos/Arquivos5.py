#wb = write binary ou seja escrever em binario
#wb = read binary ou seja ler arquivos em binario

""" escrever
with open("dados.bin", "wb") as arquivo:
    meus_texto = "aprendendo arquivos binários em python" #b para converter para binario
    meus_bytes = meus_texto.encode("Utf-8")
    arquivo.write(meus_bytes)
"""

""" ler
with open("dados.bin", "rb") as arquivo:
    conteudo_arquivo = arquivo.read()
    string_arquivo = conteudo_arquivo.decode("Utf-8")
    print(string_arquivo)
"""

import pickle
dados_jogador = {
    "nome" : "arthur",
    "nivel" : 42,
    "itens" : ["espada" , "escudo" , "pocao"] #lista dentro de um dicionario
}

with open("savegame.bin", "wb") as arquivo:
    pickle.dump(dados_jogador, arquivo)

with open("savegame.bin", "rb") as arquivo:
    jogo_carregado = pickle.load(arquivo)
    print("dados recuperados do binario", jogo_carregado)
    print(type(jogo_carregado))