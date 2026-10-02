pessoas = {"nome" : "Gustavo", "sexo" : "M", "idade" : 18 }
#print(pessoas["nome"])
#print(f"O {pessoas["nome"]} tem {pessoas["idade"]}")
#print(pessoas.keys()) # indices
#print(pessoas.values()) # valores
#print(pessoas.items()) # tudo
#del pessoas["sexo"] # apaga
#pessoas["nome"] = "Vicente" # modificar valor do nome
pessoas["peso"] = 98 # adicona ao dicionario
for k, v in pessoas.items():
    print(f"{k} = {v}") # k = indices , v = valores
