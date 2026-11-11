import zipfile
print("criando arquivo zip normal")

with zipfile.ZipFile("Execicios/pacote_normal.zip", "w") as zipf:
    zipf.write("dados.text")
    zipf.write("relatorio.text")
print("aquivo zip normal criado")