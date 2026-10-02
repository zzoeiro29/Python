print("-"*20)
print("CADASTRE UMA PESSOA")
print("-"*20)
cont_18 = cont_Homens = cont_Mulheres = 0
""" minha versao
while True:
    idade = int(input("Idade: "))
    if idade >= 18:
        cont_18 += 1
    sexo = str(input("Sexo: [M/F] "))
    if sexo in "Mm":
        cont_Homens += 1
    elif sexo in "Ff":
        if idade < 20:
            cont_Mulheres +=1
    print("-" * 20)
    escolha = str(input("Quer continuar? [S/N] : "))
    print("-" * 20)
    if escolha in "Nn":
        break
"""
#versao gunabara
while True:
    idade = int(input("Idade: "))
    if idade >= 18:
        cont_18 += 1
    sexo = " "
    while sexo not in ("MF"):
        sexo = str(input("Sexo: [M/F] ")).upper().strip() [0]
    if sexo == "M":
        cont_Homens += 1
    if sexo == "F" and idade < 20:
        cont_Mulheres += 1
    resp = " "
    while resp not in ("NS"):
        resp = str(input("Quer Continuar: [N/S] ")).upper().strip() [0]
    if resp in "Nn":
        break
print(f"Total de pessoas com mais de 18 anos: {cont_18}")
print(f"Ao Todo temos {cont_Homens} homens cadastrados " if cont_Homens > 1 else f"Ao Todo tem {cont_Homens} homen cadastrado ")
print(f"E temos {cont_Mulheres} mulheres com menos de 20 anos")