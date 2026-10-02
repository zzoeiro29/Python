conjunto = list()
pessoas = list()
maior = menor = 0
while True:
    nome = str(input("Nome: ")) # ou pessoas.append(str(input("Nome: "))
    Peso = int(input("Peso: "))
    pessoas.append(nome)
    pessoas.append(Peso)
    if len(conjunto) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]
    conjunto.append(pessoas[:])
    pessoas.clear()
    res = str(input("Quer continuar? [S/N] ")).upper()
    if res == "N":
        break
print(f"Ao todo, voce cadastrou {len(conjunto)} pessoas.")

print(f"O maior peso foi de kg {maior}. Peso de " , end="")
for p in conjunto:
    if p[1] == maior:
        print(f"{p[0]} ", end="")
print(f"\nO maior peso foi de kg {menor}. Peso de " , end="")
for p in conjunto:
    if p[1] == menor:
        print(f"{p[0]} ", end=" ")