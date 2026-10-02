lista = list()
pessoas = dict()
soma = 0
while True:
    pessoas.clear()
    pessoas["nome"] = str(input("Nome: "))
    pessoas["sexo"] = str(input("Sexo: [M/F]"))
    while not pessoas["sexo"] in "mfMF":
        print("Erro! por favor digite apenas [M/F]: ")
        pessoas["sexo"] = str(input("Por favor insira generos normais [M/F]: "))
    pessoas["idade"] = float(input("Idade: "))
    soma += pessoas["idade"]
    lista.append(pessoas.copy())
    res = str(input("Quer continuar? [S/N]"))
    while not res in "snSN":
        print("Erro! por favor digite apenas [S/N]: ")
        res = str(input("Quer continuar? [S/N]: ")).upper()
    if res in "nN":
        break
print("-=" * 30)
media = soma / len(lista)
print(f"A) Ao todo temos {len(lista)} pessoas cadastradas.")
print(f"B) A media de idade é de {media} anos.")
print(f"C) As mulheres cadastradas foram: ", end=" ")
for l in lista:
    if l["sexo"] in "fF":
        print(f"{l["nome"]}", end=" ")
print(f"D) Lista das pessoas a cima da media de idade: ")
for p in lista:
    if p["idade"] >= media:
        print("  ", end="")
        for k, v in p.items():
            print(f"  {k} = {v}; ", end="")
        print()
print("<< Encerrado >> ")
