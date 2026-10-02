contagem = {}
texto = str(input("Digite um texto: ")).split()
palavras = texto
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)



