from datetime import datetime
inf = dict()
inf["Nome"] = str(input("Nome: "))
inf["idade"] = (datetime.now().year - 1 ) - int(input("Ano de nascimento: "))
inf["ctps"] = int(input("CLT (0 se nao tem): "))
if inf["ctps"] != 0:
    inf["contrataçao"] = int(input("Ano de contrataçao: "))
    inf["salario"] = float(input("Salario: "))
    inf["aposentadoria"] = (inf["idade"] + (inf["contrataçao"] + 35) - datetime.now().year) + 1
print("-=" *30)
for k, v in inf.items():
    print(f"  - {k} tem o valor {v}")