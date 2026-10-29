import json # importando json

with open("livros.json", "r", encoding="Utf-8") as arquivo:
    livros = json.load(arquivo) # variavel livros recebe json.load(arquivo)
    # #print(livros[0]) # aquivo jason ja vem covertido para lista

print("Livros disponiveis para compra")
for livro in livros:
    if livro["em_estoque"]:
        print(livro["em_estoque"])
    #print(f"{livro["titulo"]} - {livro['preco']:.2f}") # ta imprimir o titulo e o preço
print("\n")

print("Adicionando um novo livro")
novo_livro = { # criar um novo livro para por no json
    "id": 3,
    "titulo" : "Duna",
    "autor " : "grank niga",
    "preco" : "65.00",
    "em_estoque" : True
}

livros.append(novo_livro)
print(novo_livro)

with open("Livros_atualizados.json", "w", encoding="UTF-8") as arquivo: # criar novo arquivo json
    json.dump(livros, arquivo, indent=4, ensure_ascii=False) # ensure_ascii=False vai continuar com os assentos

