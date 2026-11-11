import zipfile
import os

pasta_destino =  "arquivos_extraidos"

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

print(f"Extraido para a pasta de destino: {pasta_destino}...")

with zipfile.ZipFile("pacote_comprimido.zip", "r") as zipf:
    zipf.extractall(pasta_destino)

print("extraçao completa")