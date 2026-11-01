# ler numero de bytes da imagens
with open("box1.png", "rb") as arquivo:
    bytes_da_imagem = arquivo.read()
    print(f"A imagem foi lida! Ela tem {len(bytes_da_imagem)} bytes")
# ciar uma copia da imagem
with open("box1_copia.png", "wb") as arquivo_copia:
    arquivo_copia.write(bytes_da_imagem)
    print("Copia da imagem cirada com sucesso")