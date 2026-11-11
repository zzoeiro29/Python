import zipfile
print("criando arquivo zip normal")

with zipfile.ZipFile("pacote_comprimido.zip", "w", compression=zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("dados.text")
    zipf.write("relatorio.text")
print("aquivo zip normal criado")