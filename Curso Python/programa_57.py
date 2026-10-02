sexo = str(input("digite seu sexo (M/F): ")).upper().strip()
while sexo not in "MF": #enquanto nao estiver em MF
    sexo = str(input("Dados invalidos. Por favor, informe seu sexo: ")).upper().strip()
print("Sexo {} registrado com sucesso".format(sexo))


