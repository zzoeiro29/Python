lista_n = list()
while True:
    n = (int(input("diga um numero: ")))
    if n not in lista_n: # se o numero nao estiver na lista
        lista_n.append(n) #adiciona
        print("Valor adicionado com sucesso")
    else: # se nao diz que é duplicado
        print("Valor duplicado! Nao vou adicionar...")
    opcao = " ".upper()
    while opcao not in "SN":
        opcao = str(input("deseja continuar? [S/N] ")).upper()
    if opcao == "N":
        break
print("-="*30)
lista_n.sort()
print(f"Voce digitou os valores: {lista_n}")



