alunos = {}
# minha versao
"""
Nome = str(input("Nome: "))
Media = float(input("Media: "))
print("-="* 50)
alunos["nome"] = Nome # ou str(input("Nome: "))
alunos["media"] = Media # ou float(input("Media: "))
alunos["situacao1"] = "Aprovado"
alunos["situacao2"] = "Reprovado"
alunos["situacao3"] = "Recuperacao"
print(f"   - nome é igual a {alunos["nome"]}")
print(f"   - media é igual a {alunos["media"]}")
if alunos["media"] >= 7:
    print(f"   - Situaçao é igual a {alunos['situacao1']}")
elif 5 <= alunos["media"] < 7:
    print(f"   - Situaçao é igual a {alunos['situacao3']}")
elif alunos["media"] < 5:
    print(f"   - Situaçao é igual a {alunos['situacao2']}")
"""
# gunabara versao
alunos["nome"] = str(input("Nome: "))
alunos["media"] = float(input(f"Media de {alunos["nome"]}: "))
if alunos["media"] >= 7:
    alunos["situacao"] = "Aprovado"
elif 5 <= alunos["media"] < 7:
    alunos["situacao"] = "Recuperacao"
elif alunos["media"] < 5:
    alunos["situacao"] = "Reprovado"
print("-="* 30)
for k, v in alunos.items():
    print(f"   - {k} é igual a {v}")

