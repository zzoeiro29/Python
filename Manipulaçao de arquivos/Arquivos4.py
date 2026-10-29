import json

dados_alunos = {
    "nome": "joao",
    "nota": 9.5,
    "aprovado": True
}

texto_json = json.dumps(dados_alunos, ensure_ascii=False)
print(texto_json)

reposta_da_api = '{"curso" : "python" , "modulos" : 10 , "ativo" : true }'
dicionario = json.loads(reposta_da_api)
print(dicionario["curso"])
print(type(dicionario))