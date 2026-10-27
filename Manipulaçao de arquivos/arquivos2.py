#with open("exemplo.txt", "r+") as arquivo: # ele vai abrir ("exemplo.txt" = o arquivo, "r+" = vai escrever e ler) dentro da variavel arquivo
"""
    while True:
        bloco = arquivo.read(150)
        if not bloco:
            break
        print("Inicio Bloco")
        print(bloco)
        print("Fim Bloco")
    #arquivo.seek(10) # começa no indice 10
    #arquivo.write("Texto novo")

    for index, linha in enumerate(arquivo):
        if index < 5:
            print(linha.strip()) # remove texto e print
    #print(arquivo.read(5)) # ler arquivo
    #arquivo.seek(0) # começa do indice 0
    #print(arquivo.read(5))  # ler arquivo
    """
with open("exemplo.txt", "a") as arquivo: # a é de append uma linha de arquivo no final
    arquivo.write("\nlinha adicional no final do arquivo")