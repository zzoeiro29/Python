import zipfile

print("analisando o tamanho do zip")
with zipfile.ZipFile("pacote_comprimido.zip") as zipf:
    print(f"Arquivos encontrados: {zipf.namelist()}")
    infro = zipf.getinfo("relatorio.text")
    print(f"Tamanho original do relatorio: {infro.file_size} bytes")
    print(f"Tamanho compressao do relatorio: {infro.compress_size} bytes")